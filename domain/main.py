import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Union

import argparse
import types
from loguru import logger

import domain.modules_settings as modules_settings
from domain.modules_settings import *
from domain.utils.helpers import remove_wallet
from domain.utils.sleeping import sleep

async def run_module(module, wallet_number, key, recipient: Union[str, None] = None):
    try:
        await module(wallet_number, key, recipient)
    except Exception as e:
        logger.error(e)


def _async_run_module(module, wallet_number, key, recipient):
    asyncio.run(run_module(module, wallet_number, key, recipient))


def main(
        websites, 
        wallets, 
        quantity_threads=-1,
        wait_between_wallets_max=30,
        wait_between_wallets_min=20,
        wait_between_websites_max=20,
        wait_between_websites_min=5,
        wait_between_cycles_max=((12*60*60)+90),
        wait_between_cycles_min=((12*60*60)+5),      
        ):

    assert quantity_threads > 0, "The number of threads must be greater than 0"

    with ThreadPoolExecutor(max_workers=quantity_threads) as executor:
        while True:
            # iterate through the wallets
            for _, wallet_key in enumerate(wallets, start=1):
                # website transactions to perform at each website
                for module in websites:
                    executor.submit(
                        _async_run_module,
                        module,
                        _,
                        wallet_key,
                        None
                    )
                
                    # wait between website actions
                    time.sleep(random.randint(wait_between_websites_min, wait_between_websites_max))
                
                # wait between wallets
                time.sleep(random.randint(wait_between_wallets_min, wait_between_wallets_max))

            # wait between cycles
            time.sleep(random.randint(wait_between_cycles_min, wait_between_cycles_max))
