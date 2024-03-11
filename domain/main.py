import random
import time
from typing import Union
import asyncio

from loguru import logger


async def run_module(module, wallet_number, key, recipient: Union[str, None] = None, settings: dict = {}):
    try:
        await module(
            wallet_number, 
            key, 
            recipient, 
            from_token=settings.get('from_token'),
            to_token=settings.get('to_token'),
            min_amount=settings.get('min_amount'),
            max_amount=settings.get('max_amount'),
            slippage=settings.get('slippage'),
            all_amount=settings.get('all_amount'),
            min_percent=settings.get('min_percent'),
            max_percent=settings.get('max_percent'),
        )

    except Exception as e:
        logger.error(e)


def _async_run_module(module, wallet_number, key, recipient, settings):
    asyncio.run(run_module(module, wallet_number, key, recipient, settings))


def main(
        websites,
        wallets,
        website_settings, 
        wait_between_wallets_max=30,
        wait_between_wallets_min=20,
        wait_between_websites_max=20,
        wait_between_websites_min=5,
        wait_between_cycles_max=((12*60*60)+90),
        wait_between_cycles_min=((12*60*60)+5),      
        ):

    
    while True:
        # iterate through the wallets
        for _, wallet_key in enumerate(wallets, start=1):
            # website transactions to perform at each website
            # iterate through websites
            for tuple in zip(websites, website_settings):
                logger.info(f"Running module {tuple[0].__name__} with wallet {wallet_key}")
                _async_run_module(
                    tuple[0],
                    _,
                    wallet_key,
                    None,
                    tuple[1]
                )
            
                # wait between website actions
                random_wait = random.randint(wait_between_websites_min, wait_between_websites_max)
                logger.info(f"Waiting between websites for {random_wait} seconds")
                time.sleep(random_wait)
            
            # wait between wallets
            random_wait = random.randint(wait_between_wallets_min, wait_between_wallets_max)
            logger.info(f"Waiting between wallets for {random_wait} seconds")
            time.sleep(random_wait)

        # wait between cycles
        random_wait = random.randint(wait_between_cycles_min, wait_between_cycles_max)
        logger.info(f"Waiting between cycles for {random_wait} seconds")
        time.sleep(random_wait)
        
        # change all the settings
        logger.info(f"Switching from_token and to_token")
        for setting in website_settings:
            # ETH to USDC or back
            setting['from_token'], setting['to_token'] = setting['to_token'], setting['from_token']
