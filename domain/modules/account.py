import asyncio
import time
import random
from typing import Union, Type, Dict, Any

from hexbytes import HexBytes
from loguru import logger
from web3 import AsyncWeb3
from eth_account import Account as EthereumAccount
from web3.contract import Contract
from web3.exceptions import TransactionNotFound
from web3.middleware import async_geth_poa_middleware

from domain.config import RPC, ERC20_ABI, SCROLL_TOKENS
from domain.settings import GAS_MULTIPLIER, MAX_PRIORITY_FEE
from domain.utils.sleeping import sleep


class Account:
    def __init__(self, account_id: int, private_key: str, chain: str, recipient: str) -> None:
        self.account_id = account_id
        self.private_key = private_key
        self.chain = chain
        self.explorer = RPC[chain]["explorer"]
        self.token = RPC[chain]["token"]

        self.recipient = recipient

        self.w3 = AsyncWeb3(
            AsyncWeb3.AsyncHTTPProvider(random.choice(RPC[chain]["rpc"])),
            middlewares=[async_geth_poa_middleware]
        )

        self.account = EthereumAccount.from_key(private_key)
        self.address = self.account.address

    async def get_tx_data(self, value: int = 0, gas_price: bool = True):
        tx = {
            "chainId": await self.w3.eth.chain_id,
            "from": self.address,
            "value": value,
            "nonce": await self.w3.eth.get_transaction_count(self.address),
        }

        if gas_price:
            tx.update({"gasPrice": await self.w3.eth.gas_price})

        return tx

    async def transaction_fee(self, tx_data: dict):
        gas_price = await self.w3.eth.gas_price
        gas = await self.w3.eth.estimate_gas(tx_data)

        return int(gas * gas_price)

    def get_contract(self, contract_address: str, abi=None) -> Union[Type[Contract], Contract]:
        contract_address = self.w3.to_checksum_address(contract_address)

        if abi is None:
            abi = ERC20_ABI

        contract = self.w3.eth.contract(address=contract_address, abi=abi)

        return contract

    async def get_balance(self, contract_address: str) -> Dict:
        contract_address = self.w3.to_checksum_address(contract_address)
        contract = self.get_contract(contract_address)

        symbol = await contract.functions.symbol().call()
        decimal = await contract.functions.decimals().call()
        balance_wei = await contract.functions.balanceOf(self.address).call()

        balance = balance_wei / 10 ** decimal

        return {"balance_wei": balance_wei, "balance": balance, "symbol": symbol, "decimal": decimal}

    async def get_amount(
            self,
            from_token: str,
            min_amount: float,
            max_amount: float,
            decimal: int,
            all_amount: bool,
            min_percent: int,
            max_percent: int
    ) -> [int, float, float]:
        random_amount = round(random.uniform(min_amount, max_amount), decimal)
        random_percent = random.randint(min_percent, max_percent)
        percent = 1 if random_percent == 100 else random_percent / 100

        if from_token == "ETH":
            balance = await self.w3.eth.get_balance(self.address)

            amount_wei = int(balance * percent) if all_amount else self.w3.to_wei(random_amount, "ether")
            amount = self.w3.from_wei(int(balance * percent), "ether") if all_amount else random_amount
        else:
            # all_amount = True
            balance = await self.get_balance(SCROLL_TOKENS[from_token])
            amount_wei = int(balance["balance_wei"] * percent) \
                if all_amount else int(random_amount * 10 ** balance["decimal"])
            amount = balance["balance"] * percent if all_amount else random_amount
            balance = balance["balance_wei"]

        return amount_wei, amount, balance

    async def check_allowance(self, token_address: str, contract_address: str) -> int:
        token_address = self.w3.to_checksum_address(token_address)
        contract_address = self.w3.to_checksum_address(contract_address)

        contract = self.w3.eth.contract(address=token_address, abi=ERC20_ABI)
        amount_approved = await contract.functions.allowance(self.address, contract_address).call()

        return amount_approved

    async def approve(self, amount: float, token_address: str, contract_address: str) -> None:
        token_address = self.w3.to_checksum_address(token_address)
        contract_address = self.w3.to_checksum_address(contract_address)

        contract = self.w3.eth.contract(address=token_address, abi=ERC20_ABI)

        allowance_amount = await self.check_allowance(token_address, contract_address)

        if amount > allowance_amount or amount == 0:
            logger.success(f"[{self.account_id}][{self.address}] Make approve")

            approve_amount = 2 ** 128 if amount > allowance_amount else 0

            tx_data = await self.get_tx_data()

            # logger.info(f"contract_address-----{contract_address}")
            # logger.info(f"approve_amount-----{approve_amount}")
            try:
              transaction = await contract.functions.approve(
                  contract_address,
                  approve_amount
              ).build_transaction(tx_data)

              # logger.info(f"transaction========{transaction}")
            except Exception as e:
              logger.error(f"Output while dealing with func:await contract.functions.approve under approve function{e} ")
              transaction = await contract.functions.approve(
                  contract_address,
                  approve_amount
              ).build_transaction(tx_data)

            try:
              signed_txn = await self.sign(transaction)
            except Exception as e:
              logger.error(f"Output while dealing with func:await self.sign(transaction) under approve function {e} ")
              signed_txn = await self.sign(transaction)

            try:
              txn_hash = await self.send_raw_transaction(signed_txn)
            except Exception as e:
              logger.error(f"Output while dealing with func:await self.send_raw_transaction(signed_txn) under approve function {e} ")
              txn_hash = await self.send_raw_transaction(signed_txn)

            try:
              await self.wait_until_tx_finished(txn_hash.hex())
            except Exception as e:
              logger.error(f"Output while dealing with func:await self.wait_until_tx_finished(txn_hash.hex()) under approve function {e} ")

            await sleep(5, 20)

    # static approve function to test or run with insufficient funds
    # async def approve(self, amount: float, token_address: str, contract_address: str) -> None:
    #     token_address = self.w3.to_checksum_address(token_address)
    #     contract_address = self.w3.to_checksum_address(contract_address)

    #     contract = self.w3.eth.contract(address=token_address, abi=ERC20_ABI)

    #     allowance_amount = await self.check_allowance(token_address, contract_address)

    #     logger.info(f"allowance_amount{allowance_amount}")

    #     if amount > allowance_amount or amount == 0:
    #         logger.success(f"[{self.account_id}][{self.address}] Make approve")

    #         approve_amount = 2 ** 128

    #         tx_data = await self.get_tx_data()

    #         try:
    #           # transaction = await contract.functions.approve(
    #           #     contract_address,
    #           #     approve_amount
    #           # ).build_transaction(tx_data)
    #           transaction = {'gas': 187199, 'chainId': 534352, 'from': '0x3f29f6815f12e33cDEC040a453cd9120525dB4b9', 'value': 100000000000000, 'nonce': 3, 'gasPrice': 550000000, 'to': '0xAA111C62cDEEf205f70E6722D1E22274274ec12F', 'data': '0x67ffb66a00000000000000000000000000000000000000000000000000000000000504fb00000000000000000000000000000000000000000000000000000000000000800000000000000000000000003f29f6815f12e33cdec040a453cd9120525db4b900000000000000000000000000000000000000000000000000000000661c66c70000000000000000000000000000000000000000000000000000000000000001000000000000000000000000530000000000000000000000000000000000000400000000000000000000000006efdbff2a14a7c8e15944d1f4a48f9f95f663a40000000000000000000000000000000000000000000000000000000000000000'}

    #         except Exception as e:
    #           logger.error(f"Output while dealing with func:await contract.functions.approve under approve function{e} ")
    #           transaction = await contract.functions.approve(
    #               contract_address,
    #               approve_amount
    #           ).build_transaction(tx_data)

    #         logger.info(f"transaction on approve : {transaction}")

    #         try:
    #           signed_txn = await self.sign(transaction)
    #         except Exception as e:
    #           logger.error(f"Output while dealing with func:await self.sign(transaction) under approve function {e} ")
    #           signed_txn = await self.sign(transaction)

    #         try:
    #           txn_hash = await self.send_raw_transaction(signed_txn)
    #         except Exception as e:
    #           logger.error(f"Output while dealing with func:await self.send_raw_transaction(signed_txn) under approve function {e} ")
    #           txn_hash = await self.send_raw_transaction(signed_txn)

    #         try:
    #           await self.wait_until_tx_finished(txn_hash.hex())
    #         except Exception as e:
    #           logger.error(f"Output while dealing with func:await self.wait_until_tx_finished(txn_hash.hex()) under approve function {e} ")

    #         await sleep(5, 20)


    async def wait_until_tx_finished(self, hash: str, max_wait_time=180) -> None:
        start_time = time.time()
        while True:
            try:
                receipts = await self.w3.eth.get_transaction_receipt(hash)
                status = receipts.get("status")
                if status == 1:
                    logger.success(f"[{self.account_id}][{self.address}] {self.explorer}{hash} successfully!")
                    return
                elif status is None:
                    await asyncio.sleep(0.3)
                else:
                    logger.error(f"[{self.account_id}][{self.address}] {self.explorer}{hash} transaction failed!")
                    return
            except TransactionNotFound:
                if time.time() - start_time > max_wait_time:
                    print(f'FAILED TX: {hash}')
                    return
                await asyncio.sleep(1)


# static sign function to run with insufficient funds
    # async def sign(self, transaction) -> Any:
    #     # if transaction.get("gasPrice", None) is None:


    #     max_priority_fee_per_gas = self.w3.to_wei(MAX_PRIORITY_FEE["ethereum"], "gwei")
    #     max_fee_per_gas = await self.w3.eth.gas_price


    #     transaction.update(
    #         {
    #             "maxPriorityFeePerGas": max_priority_fee_per_gas,
    #             "maxFeePerGas": max_fee_per_gas,
    #         }
    #     )

    #     logger.info(f"transaction under sign--{transaction}")

    #     try:
    #         # Add nonce if it's not already present in the transaction
    #         if 'nonce' not in transaction:
    #             transaction['nonce'] = 3

    #         gas = 10000000000000000
    #         gas = int(gas * GAS_MULTIPLIER)

    #         logger.info(f"gas------- {gas}")

    #         transaction.update({"gas": gas})

    #         logger.info(f"transaction after updating gas------:{transaction}")

    #         logger.info(f"private key--------:{self.private_key}")

    #         signed_txn = self.w3.eth.account.sign_transaction(transaction, self.private_key)
    #         return signed_txn

    #     except Exception as e:
    #         logger.error(f"Error in sign_transaction: {e}")
    #         return None

    async def sign(self, transaction) -> Any:
        if transaction.get("gasPrice", None) is None:
            max_priority_fee_per_gas = self.w3.to_wei(MAX_PRIORITY_FEE["ethereum"], "gwei")
            max_fee_per_gas = await self.w3.eth.gas_price

            transaction.update(
                {
                    "maxPriorityFeePerGas": max_priority_fee_per_gas,
                    "maxFeePerGas": max_fee_per_gas,
                }
            )

        # logger.info(f"transaction under sign--{transaction}")

        gas = await self.w3.eth.estimate_gas(transaction)
        gas = int(gas * GAS_MULTIPLIER)
        # logger.info(f"gas------- {gas}")
        transaction.update({"gas": gas})
        # logger.info(f"transaction after updating gas------:{transaction}")

        try:
            signed_txn = self.w3.eth.account.sign_transaction(transaction, self.private_key)
        except Exception as e:
            logger.error(f"Error in sign_transaction: {e}")
            signed_txn = self.w3.eth.account.sign_transaction(transaction, self.private_key)


        return signed_txn

    async def send_raw_transaction(self, signed_txn) -> HexBytes:
        txn_hash = await self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return txn_hash
