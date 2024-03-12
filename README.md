<div align="center">
  <img src="https://i.imgur.com/Vaah2gJ.png"  />
  <h1>Run Scroll Swaps Script</h1>
  <p>This software automates swap farming on the Scroll network, providing access to a CLI script that exposes a highly-customizable automated swaping system with randomization.</p>
</div>

---

<b>Authors: John Reyes; OxBlackfish</b>

Heavily adapted from Scroll Soft by https://t.me/sybilwave

---
<h2>🚀 Installation</h2>

```
# clone with https
git clone https://github.com/napindic/scroll

# or clone with ssh
git clone git@github.com:napindc/scroll.git

cd scroll

pip install -r requirements.txt

~/scroll$ python run_swaps.py --wallets WALLET_KEY1 WALLET_KEY2 WALLET_KEYN
```
---
<>🚨 Features</h2>

* emables running automated trades on multiple websites as a single python command
* accepts a single or multiple wallet private keys to perform swaps
* uses a dynamically randomizing schedule to execute trades and recycle wallets
* easily configurable - command line arguments expose the abilty to change the randomization schedules, amount to swap, and token to swap
* automatically cycles between swapping from ETH to USDC and then back from USDC to ETH

---


---
<h2>⚙️ Settings</h2>

1) All setting are set at the command line, they can be shown again with the command:
```
$ python run_swaps.py -h
```

Note: the script has reasonable defaults

2) The rpc.json file at the path domain/data/rpc.json we can change the rpc to a personal or private rpc

---
<h2>Default Settings</h2>

By default this script will execute the following:

* 4 swaps per cycle on Skydrome, Zebra, SyncSwap, and XYSwap
* Randomize execution with between 5-20 minutes between websites, 20-30 minutes between wallets, and a random number of minutes less than 90 after 12 hours before recycle the wallets in the reverse direction
* starts swapping from USDC to ETH before reversing after the first cycle and waits complete

---
<h3>Settings in detail</h2>

  -h, --help            show this help message and exit
  --websites WEBSITES   The transaction types at the website you want to perform from the available actions
  -l, --list            List all available actions
  -R, --random          Use wallets in a random order

Wallets:
  --wallet WALLET       The wallet you want to use
  --wallets WALLETS     The wallets you want to use

Wait Between Wallets:
  --wait-between-wallets-max-seconds WAIT_BETWEEN_WALLETS_MAX_SECONDS
                        The maximum time in seconds to wait between wallets default: 1800 seconds (30 minutes)
  --wait-between-wallets-min-seconds WAIT_BETWEEN_WALLETS_MIN_SECONDS
                        The minimum time in seconds to wait between wallets default: 1200 seconds (20 minutes)

Wait Between Websites:
  --wait-between-websites-max-seconds WAIT_BETWEEN_WEBSITES_MAX_SECONDS
                        The maximum time in seconds to wait between websites default: 1200 seconds (20 minutes)
  --wait-between-websites-min-seconds WAIT_BETWEEN_WEBSITES_MIN_SECONDS
                        The minimum time in seconds to wait between websites default: 300 seconds (5 minutes)

Wait Between Cycles:
  --wait-between-cycles-max-seconds WAIT_BETWEEN_CYCLES_MAX_SECONDS
                        The maximum time in seconds to wait between cycles default: 48600 (12 hours and 90 minutes)
  --wait-between-cycles-min-seconds WAIT_BETWEEN_CYCLES_MIN_SECONDS
                        The minimum time in seconds to wait between cycles default: 43500 (12 hours and 5 minutes)

Swap Skydrome Settings:
  --skydrome-from-token SKYDROME_FROM_TOKEN
                        The token you want to swap from
  --skydrome-to-token SKYDROME_TO_TOKEN
                        The token you want to swap to
  --skydrome-min-amount SKYDROME_MIN_AMOUNT
                        The amount of the token you want to swap
  --skydrome-max-amount SKYDROME_MAX_AMOUNT
                        The amount of the token you want to swap
  --skydrome-decimal SKYDROME_DECIMAL
                        The decimal of the token you want to swap
  --skydrome-slippage SKYDROME_SLIPPAGE
                        The slippage of the token you want to swap
  --skydrome-all-amount SKYDROME_ALL_AMOUNT
                        Swap all the amount of the token you want to swap
  --skydrome-min-percent SKYDROME_MIN_PERCENT
                        The minimum percent of the token you want to swap
  --skydrome-max-percent SKYDROME_MAX_PERCENT
                        The maximum percent of the token you want to swap

Swap Zebra Settings:
  --zebra-from-token ZEBRA_FROM_TOKEN
                        The token you want to swap from
  --zebra-to-token ZEBRA_TO_TOKEN
                        The token you want to swap to
  --zebra-min-amount ZEBRA_MIN_AMOUNT
                        The amount of the token you want to swap
  --zebra-max-amount ZEBRA_MAX_AMOUNT
                        The amount of the token you want to swap
  --zebra-decimal ZEBRA_DECIMAL
                        The decimal of the token you want to swap
  --zebra-slippage ZEBRA_SLIPPAGE
                        The slippage of the token you want to swap
  --zebra-all-amount ZEBRA_ALL_AMOUNT
                        Swap all the amount of the token you want to swap
  --zebra-min-percent ZEBRA_MIN_PERCENT
                        The minimum percent of the token you want to swap
  --zebra-max-percent ZEBRA_MAX_PERCENT
                        The maximum percent of the token you want to swap

Swap SyncSwap Settings:
  --syncswap-from-token SYNCSWAP_FROM_TOKEN
                        The token you want to swap from
  --syncswap-to-token SYNCSWAP_TO_TOKEN
                        The token you want to swap to
  --syncswap-min-amount SYNCSWAP_MIN_AMOUNT
                        The amount of the token you want to swap
  --syncswap-max-amount SYNCSWAP_MAX_AMOUNT
                        The amount of the token you want to swap
  --syncswap-decimal SYNCSWAP_DECIMAL
                        The decimal of the token you want to swap
  --syncswap-slippage SYNCSWAP_SLIPPAGE
                        The slippage of the token you want to swap
  --syncswap-all-amount SYNCSWAP_ALL_AMOUNT
                        Swap all the amount of the token you want to swap
  --syncswap-min-percent SYNCSWAP_MIN_PERCENT
                        The minimum percent of the token you want to swap
  --syncswap-max-percent SYNCSWAP_MAX_PERCENT
                        The maximum percent of the token you want to swap

Swap XYSwap Settings:
  --xyswap-from-token XYSWAP_FROM_TOKEN
                        The token you want to swap from
  --xyswap-to-token XYSWAP_TO_TOKEN
                        The token you want to swap to
  --xyswap-min-amount XYSWAP_MIN_AMOUNT
                        The amount of the token you want to swap
  --xyswap-max-amount XYSWAP_MAX_AMOUNT
                        The amount of the token you want to swap
  --xyswap-decimal XYSWAP_DECIMAL
                        The decimal of the token you want to swap
  --xyswap-slippage XYSWAP_SLIPPAGE
                        The slippage of the token you want to swap
  --xyswap-all-amount XYSWAP_ALL_AMOUNT
                        Swap all the amount of the token you want to swap
  --xyswap-min-percent XYSWAP_MIN_PERCENT
                        The minimum percent of the token you want to swap
  --xyswap-max-percent XYSWAP_MAX_PERCENT
                        The maximum percent of the token you want to swap