import asyncio, loguru , tabulate, requests,hexbytes, hashlib, aiohttp, eth_abi, eth_utils, eth_typing, web3
import domain
import argparse
import types
import sys,os
# other depending modules


import domain.modules_settings as modules_settings

import random
import json
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

class SwapRunner():
    def __init__(self, websites=[], wallets=[], website_settings=[],
                 wait_between_wallets_max=30, wait_between_wallets_min=20,
                 wait_between_websites_max=20, wait_between_websites_min=5,
                 wait_between_cycles_max=((12*60*60)+90), wait_between_cycles_min=((12*60*60)+5)):
        self.websites = websites
        self.wallets = wallets
        self.website_settings = website_settings
        self.wait_between_wallets_max = wait_between_wallets_max
        self.wait_between_wallets_min = wait_between_wallets_min
        self.wait_between_websites_max = wait_between_websites_max
        self.wait_between_websites_min = wait_between_websites_min
        self.wait_between_cycles_max = wait_between_cycles_max
        self.wait_between_cycles_min = wait_between_cycles_min
        # skydrome settings

        # syncswap settings

        # xyswap settings

    def list_websites(self):
        # Get all attributes of the module
        module_attributes = dir(modules_settings)

        # Filter out only the functions
        functions = [attr for attr in module_attributes if callable(getattr(modules_settings, attr)) and not attr.startswith("__") and attr[0].islower()]

        # Print the names of the functions
        print("Available websites:")
        # print("Functions in the module:")
        for func in functions:
            print(func)

    def run(self):
        if "tx_checker" in self.websites:
            domain.modules_settings.get_tx_count(wallets)
        else:

            domain.main(
                self.websites,
                self.wallets,
                self.website_settings,
                wait_between_wallets_max=self.wait_between_wallets_max,
                wait_between_wallets_min=self.wait_between_wallets_min,
                wait_between_websites_max=self.wait_between_websites_max,
                wait_between_websites_min=self.wait_between_websites_min,
                wait_between_cycles_max=self.wait_between_cycles_max,
                wait_between_cycles_min=self.wait_between_cycles_min
            )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--websites", default='swap_syncswap swap_skydrome swap_zebra swap_xyswap', help="The transaction types at the website you want to perform")
    parser.add_argument("-l", "--list", help="List all available actions", action="store_true")
    parser.add_argument("-R", "--random", help="Use wallets in a random order", action="store_true")

    wallet_group = parser.add_argument_group("Wallets")
    wallet_xclsv_group = wallet_group.add_mutually_exclusive_group()
    wallet_xclsv_group.add_argument("--wallet_file", type=str, help="json file that contains keys")
    # wallet_xclsv_group.add_argument("--wallet", help="The wallet you want to use")
    # wallet_xclsv_group.add_argument("--wallets", type=str, help="The wallets you want to use")

    wait_between_wallets_group = parser.add_argument_group("Wait Between Wallets")
    wait_between_wallets_group.add_argument("--wait-between-wallets-max-seconds", type=int, default=(30*60), help="The maximum time in seconds to wait between wallets default: 1800 seconds (30 minutes)")
    wait_between_wallets_group.add_argument("--wait-between-wallets-min-seconds", type=int, default=(20*60), help="The minimum time in seconds to wait between wallets default: 1200 seconds (20 minutes)")

    wait_between_websites_group = parser.add_argument_group("Wait Between Websites")
    wait_between_websites_group.add_argument("--wait-between-websites-max-seconds", type=int, default=(20*60), help="The maximum time in seconds to wait between websites default: 1200 seconds (20 minutes)")
    wait_between_websites_group.add_argument("--wait-between-websites-min-seconds", type=int, default=(5*60), help="The minimum time in seconds to wait between websites default: 300 seconds (5 minutes)")

    wait_between_cycles_group = parser.add_argument_group("Wait Between Cycles")
    wait_between_cycles_group.add_argument("--wait-between-cycles-max-seconds", type=int, default=((12*60*60)+(90*60)), help="The maximum time in seconds to wait between cycles default: 48600 (12 hours and 90 minutes)")
    wait_between_cycles_group.add_argument("--wait-between-cycles-min-seconds", type=int, default=((12*60*60)+(5*60)), help="The minimum time in seconds to wait between cycles default: 43500 (12 hours and 5 minutes)")

    swap_skydrome_group = parser.add_argument_group("Swap Skydrome Settings")
    swap_skydrome_group.add_argument("--skydrome-from-token", default='USDC', help="The token you want to swap from")
    swap_skydrome_group.add_argument("--skydrome-to-token", default='ETH', help="The token you want to swap to")
    swap_skydrome_group.add_argument("--skydrome-min-amount", type=float, default=0.0001, help="The amount of the token you want to swap")
    swap_skydrome_group.add_argument("--skydrome-max-amount", type=float, default=0.0002, help="The amount of the token you want to swap")
    swap_skydrome_group.add_argument("--skydrome-decimal", type=int, default=6, help="The decimal of the token you want to swap")
    swap_skydrome_group.add_argument("--skydrome-slippage", type=int, default=1, help="The slippage of the token you want to swap")
    swap_skydrome_group.add_argument("--skydrome-all-amount", type=bool, default=False, help="Swap all the amount of the token you want to swap")
    swap_skydrome_group.add_argument("--skydrome-min-percent", type=int, default=100, help="The minimum percent of the token you want to swap")
    swap_skydrome_group.add_argument("--skydrome-max-percent", type=int, default=100, help="The maximum percent of the token you want to swap")

    swap_zebra_group = parser.add_argument_group("Swap Zebra Settings")
    swap_zebra_group.add_argument("--zebra-from-token", default='USDC', help="The token you want to swap from")
    swap_zebra_group.add_argument("--zebra-to-token", default='ETH', help="The token you want to swap to")
    swap_zebra_group.add_argument("--zebra-min-amount", type=float, default=0.0001, help="The amount of the token you want to swap")
    swap_zebra_group.add_argument("--zebra-max-amount", type=float, default=0.0002, help="The amount of the token you want to swap")
    swap_zebra_group.add_argument("--zebra-decimal", type=int, default=6, help="The decimal of the token you want to swap")
    swap_zebra_group.add_argument("--zebra-slippage", type=int, default=1, help="The slippage of the token you want to swap")
    swap_zebra_group.add_argument("--zebra-all-amount", type=bool, default=False, help="Swap all the amount of the token you want to swap")
    swap_zebra_group.add_argument("--zebra-min-percent", type=int, default=100, help="The minimum percent of the token you want to swap")
    swap_zebra_group.add_argument("--zebra-max-percent", type=int, default=100, help="The maximum percent of the token you want to swap")

    swap_syncswap_group = parser.add_argument_group("Swap SyncSwap Settings")
    swap_syncswap_group.add_argument("--syncswap-from-token", default='USDC', help="The token you want to swap from")
    swap_syncswap_group.add_argument("--syncswap-to-token", default='ETH', help="The token you want to swap to")
    swap_syncswap_group.add_argument("--syncswap-min-amount", type=float, default=0.0001, help="The amount of the token you want to swap")
    swap_syncswap_group.add_argument("--syncswap-max-amount", type=float, default=0.0002, help="The amount of the token you want to swap")
    swap_syncswap_group.add_argument("--syncswap-decimal", type=int, default=6, help="The decimal of the token you want to swap")
    swap_syncswap_group.add_argument("--syncswap-slippage", type=int, default=1, help="The slippage of the token you want to swap")
    swap_syncswap_group.add_argument("--syncswap-all-amount", type=bool, default=False, help="Swap all the amount of the token you want to swap")
    swap_syncswap_group.add_argument("--syncswap-min-percent", type=int, default=100, help="The minimum percent of the token you want to swap")
    swap_syncswap_group.add_argument("--syncswap-max-percent", type=int, default=100, help="The maximum percent of the token you want to swap")

    swap_xyswap_group = parser.add_argument_group("Swap XYSwap Settings")
    swap_xyswap_group.add_argument("--xyswap-from-token", default='USDC', help="The token you want to swap from")
    swap_xyswap_group.add_argument("--xyswap-to-token", default='ETH', help="The token you want to swap to")
    swap_xyswap_group.add_argument("--xyswap-min-amount", type=float, default=0.0001, help="The amount of the token you want to swap")
    swap_xyswap_group.add_argument("--xyswap-max-amount", type=float, default=0.0002, help="The amount of the token you want to swap")
    swap_xyswap_group.add_argument("--xyswap-decimal", type=int, default=6, help="The decimal of the token you want to swap")
    swap_xyswap_group.add_argument("--xyswap-slippage", type=int, default=1, help="The slippage of the token you want to swap")
    swap_xyswap_group.add_argument("--xyswap-all-amount", type=bool, default=False, help="Swap all the amount of the token you want to swap")
    swap_xyswap_group.add_argument("--xyswap-min-percent", type=int, default=100, help="The minimum percent of the token you want to swap")
    swap_xyswap_group.add_argument("--xyswap-max-percent", type=int, default=100, help="The maximum percent of the token you want to swap")


    args = parser.parse_args()

    if args.list:
        swap_runner = SwapRunner()
        swap_runner.list_websites()
        sys.exit()
    else:

        assert args.websites, "You must provide a website transaction type to perform"
        assert all([website in dir(modules_settings) for website in args.websites.split(" ")]), f"Action {args.websites} is not supported"

        websites = [domain.modules_settings.__dict__[action] for action in args.websites.split(" ")]
        assert type(websites[0]) == types.FunctionType, f"Action {args.action} is not supported"

        # assert that either the wallet or list of wallets is provided
        assert args.wallet_file, "You must provide a wallet to use"

        website_settings = [
            {
                "from_token": args.skydrome_from_token,
                "to_token": args.skydrome_to_token,
                "min_amount": args.skydrome_min_amount,
                "max_amount": args.skydrome_max_amount,
                "slippage": args.skydrome_slippage,
                "all_amount": args.skydrome_all_amount,
                "min_percent": args.skydrome_min_percent,
                "max_percent": args.skydrome_max_percent,
            },
            {
                "from_token": args.zebra_from_token,
                "to_token": args.zebra_to_token,
                "min_amount": args.zebra_min_amount,
                "max_amount": args.zebra_max_amount,
                "slippage": args.zebra_slippage,
                "all_amount": args.zebra_all_amount,
                "min_percent": args.zebra_min_percent,
                "max_percent": args.zebra_max_percent,
            },
            {
                "from_token": args.syncswap_from_token,
                "to_token": args.syncswap_to_token,
                "min_amount": args.syncswap_min_amount,
                "max_amount": args.syncswap_max_amount,
                "slippage": args.syncswap_slippage,
                "all_amount": args.syncswap_all_amount,
                "min_percent": args.syncswap_min_percent,
                "max_percent": args.syncswap_max_percent,
            },
            {
                "from_token": args.xyswap_from_token,
                "to_token": args.xyswap_to_token,
                "min_amount": args.xyswap_min_amount,
                "max_amount": args.xyswap_max_amount,
                "slippage": args.xyswap_slippage,
                "all_amount": args.xyswap_all_amount,
                "min_percent": args.xyswap_min_percent,
                "max_percent": args.xyswap_max_percent,
            }
        ]

        wallets = []
        # if args.wallets:
        #     wallets = [key for key in args.wallets.split(" ")]
        # elif args.wallet:
        #     wallets = [args.wallet]

        # parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))  # Parent directory
        # grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))  # Grandparent directory
        # file_path = os.path.join(grandparent_dir, 'scroll.json')

        if os.path.exists(args.wallet_file):
            os.environ['wallet_file_path'] = args.wallet_file
            # Load keys from the JSON file
            with open(args.wallet_file, 'r') as f:
                keys_data = json.load(f)

              # Decrypt each key and add it to the wallets list
                for key_info in keys_data['keysDetails']:
                    encrypted_data = key_info['keysDetails']['encryptedData']
                    encryption_key = key_info['keysDetails']['key']
                    iv = key_info['keysDetails']['uuid']

                    # Base64 decode the encrypted data and encryption key
                    encrypted_data_bytes = bytes.fromhex(encrypted_data)
                    encryption_key_bytes = bytes.fromhex(encryption_key)
                    iv_bytes = bytes.fromhex(iv)

                    # Decrypt the data
                    cipher = AES.new(encryption_key_bytes, AES.MODE_CBC, iv=iv_bytes)
                    decrypted_data = unpad(cipher.decrypt(encrypted_data_bytes), AES.block_size)

                    # Convert the decrypted data from bytes to string
                    decrypted_key = decrypted_data.decode('utf-8')
                    # Add the decrypted key to the wallets list
                    wallets.append(decrypted_key)


        if args.random:
            random.shuffle(wallets)

        swap_runner = SwapRunner(
                                websites=websites,
                                wallets=wallets,
                                website_settings=website_settings,
                                wait_between_wallets_max=args.wait_between_wallets_max_seconds,
                                wait_between_wallets_min=args.wait_between_wallets_min_seconds,
                                wait_between_websites_max=args.wait_between_websites_max_seconds,
                                wait_between_websites_min=args.wait_between_websites_min_seconds,
                                wait_between_cycles_max=args.wait_between_cycles_max_seconds,
                                wait_between_cycles_min=args.wait_between_cycles_min_seconds
                                )

        swap_runner.run()
