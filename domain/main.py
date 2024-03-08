import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Union

import argparse
import types
from loguru import logger

import modules_settings
from modules_settings import *
from utils.helpers import remove_wallet
from utils.sleeping import sleep

SLEEP_FROM = -1 # Seconds
SLEEP_TO = -1 # Seconds

async def run_module(module, account_id, key, recipient: Union[str, None] = None):
    assert SLEEP_FROM > 0, "The minimum time in seconds to sleep between transactions must be greater than 0"
    assert SLEEP_TO > 0, "The maximum time in seconds to sleep between transactions must be greater than 0"

    try:
        await module(account_id, key, recipient)
    except Exception as e:
        logger.error(e)

    await sleep(SLEEP_FROM, SLEEP_TO)


def _async_run_module(module, account_id, key, recipient):
    asyncio.run(run_module(module, account_id, key, recipient))


def main(module, wallets, quantity_threads=-1, 
         thread_sleep_from=-1, thread_sleep_to=-1):

    assert quantity_threads > 0, "The number of threads must be greater than 0"
    assert thread_sleep_from > 0, "The minimum time in seconds to sleep between transactions must be greater than 0"
    assert thread_sleep_to > 0, "The maximum time in seconds to sleep between transactions must be greater than 0"

    with ThreadPoolExecutor(max_workers=quantity_threads) as executor:
        for _, wallet_key in enumerate(wallets, start=1):
            executor.submit(
                _async_run_module,
                module,
                _,
                wallet_key,
                None
            )
            time.sleep(random.randint(thread_sleep_from, thread_sleep_to))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="The transaction type you want to perform")
    parser.add_argument("-R", "--random", help="Use wallets in a random order", action="store_true")
    wallet_group = parser.add_argument_group("Wallets")
    wallet_xclsv_group = wallet_group.add_mutually_exclusive_group(required=True)
    wallet_xclsv_group.add_argument("--wallet", help="The wallet you want to use")
    wallet_xclsv_group.add_argument("--wallets", type=list, help="The wallets you want to use")
    thread_settings_group = parser.add_argument_group("Thread Settings")
    thread_settings_group.add_argument("--threads", type=int, default=1, help="The number of threads to use")
    thread_settings_group.add_argument("--thread-sleep-from", type=int, default=5, help="The minimum time in seconds to sleep between transactions")
    thread_settings_group.add_argument("--thread-sleep-to", type=int, default=5, help="The maximum time in seconds to sleep between transactions")
    execution_cadence_group = parser.add_argument_group("Execution Cadence Settings")
    execution_cadence_group.add_argument("--sleep-from", type=int, default=500, help="The minimum time in seconds to sleep between transactions")
    execution_cadence_group.add_argument("--sleep-to", type=int, default=1000, help="The maximum time in seconds to sleep between transactions")
    
    args = parser.parse_args()

    assert args.action, "You must provide an action to perform"
    assert args.action in modules_settings.__dict__, f"Action {args.action} is not supported"

    module = modules_settings.__dict__[args.action]
    assert type(module) == types.FunctionType, f"Action {args.action} is not supported"

    SLEEP_FROM = args.sleep_from
    SLEEP_TO = args.sleep_to

    # assert that either the wallet or list of wallets is provided
    assert args.wallet or args.wallets, "You must provide a wallet to use"

    wallets = []
    if args.wallets:
        wallets = args.wallets
    elif args.wallet:
        wallets = [args.wallet]

    if args.random:
        random.shuffle(wallets)

    logger.add("logging.log")

    if module == "tx_checker":
        modules_settings.get_tx_count()
    else:
        main(
             module, 
             wallets, 
             quantity_threads=args.threads, 
             thread_sleep_from=args.thread_sleep_from, 
             thread_sleep_to=args.thread_sleep_to
             )

