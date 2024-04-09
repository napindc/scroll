import random
import time
from typing import Union
import asyncio
from eth_account import Account as EthereumAccount
from loguru import logger
from .modules_settings import handle_app_expiration
from .settings import managingEnvironment

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

    is_expired = handle_app_expiration()
    if is_expired:
        return



    while True:

        logger.info(f"Selected wallets: {len(wallets)}")
        # iterate through the wallets
        for _, wallet_key in enumerate(wallets, start=1):
            # website transactions to perform at each website

            wallet_address = EthereumAccount.from_key(wallet_key).address
            logger.info(f"Running module {websites[0].__name__}")
            logger.info(f"With wallet {wallet_address[:6]}...{wallet_address[-6:]}")

            _async_run_module(
                  websites[0],
                  _,
                  wallet_key,
                  None,
                  website_settings[0]
              )

            env = managingEnvironment["python_running_env"]
              # random wait to swap back
            random_wait = random.randint(managingEnvironment[env]["waitTimeBetweenSwapBack"]["from"], managingEnvironment[env]["waitTimeBetweenSwapBack"]["to"])
            minutes = int((random_wait % managingEnvironment['totalSecond']) // managingEnvironment['totalMinutes'])

            logger.info(f"Randomly wait between switching from {website_settings[0]['from_token']} to {website_settings[0]['to_token']} for {minutes} minutes")
            time.sleep(random_wait)
            website_settings[0]['from_token'], website_settings[0]['to_token'] = website_settings[0]['to_token'], website_settings[0]['from_token']

            # After Switching running the module again
            # logger.info(f"Running module {websites[0].__name__} with wallet {wallet_key}")
            _async_run_module(
                  websites[0],
                  _,
                  wallet_key,
                  None,
                  website_settings[0]
              )

            # Switch the token back to original for next wallet
            website_settings[0]['from_token'], website_settings[0]['to_token'] = website_settings[0]['to_token'], website_settings[0]['from_token']

            #----- for multiple website we comment this for now ------
             # iterate through websites
            # for tuple in zip(websites, website_settings):
            #     logger.info(f"Running module {tuple[0].__name__} with wallet {wallet_key}")
            #     _async_run_module(
            #         tuple[0],
            #         _,
            #         wallet_key,
            #         None,
            #         tuple[1]
            #     )


                # wait between website actions
                # random_wait = random.randint(wait_between_websites_min, wait_between_websites_max)
                # logger.info(f"Waiting between websites for {random_wait/3600} hours")
                # time.sleep(random_wait)

          #---------- multiple website comment end ----------

            # wait between wallets
            if len(wallets) > 1:
              random_wait = random.randint(wait_between_wallets_min, wait_between_wallets_max)
              hours = int(random_wait //  managingEnvironment['totalSecond'])
              minutes = int((random_wait %  managingEnvironment['totalSecond']) // managingEnvironment['totalMinutes'])

              if hours == 0:
                  logger.info(f"Waiting between wallets for {minutes} minutes.")
              else:
                  logger.info(f"Waiting between wallets for {hours} hours and {minutes} minutes.")
              time.sleep(random_wait)

        # wait between cycles
        random_wait = random.randint(wait_between_cycles_min, wait_between_cycles_max)
        hours = int(random_wait // managingEnvironment['totalSecond'])
        minutes = int((random_wait % managingEnvironment['totalSecond']) // managingEnvironment['totalMinutes'])
        if hours == 0:
                logger.info(f"Waiting between cycles for {minutes} minutes.")
        else:
            logger.info(f"Waiting between cycles for {hours} hours and {minutes} minutes.")

        while random_wait >= 3600:  # If the wait time is more than equal to 1 hour
            hours_remaining = int(random_wait // 3600)
            if hours_remaining >= 1:  # Log time every hour
                logger.info(f"{hours_remaining} hours left until next swap")
            # Sleep for 1 hour
            time.sleep(3600)
            # Decrease the remaining time by 1 hour
            random_wait -= 3600

        # change all the settings

        # for setting in website_settings:
        #     # ETH to USDC or back
        #     setting['from_token'], setting['to_token'] = setting['to_token'], setting['from_token']




