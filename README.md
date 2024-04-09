<div align="center">
  <img src="https://i.imgur.com/Vaah2gJ.png"  />
  <h1>Run Scroll Swaps Script</h1>
  <p>This software automates swap farming on the Scroll network, providing access to a CLI script that exposes a highly-customizable automated swaping system with randomization.</p>
</div>

---

<b>Authors: <a href="https://github.com/jareyes409">John Reyes</a>; <a href="https://github.com/0xBlackfish">OxBlackfish</a></b>

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
<h2>🚨 Features</h2>

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

  <p>-h, --help</p>            
  <em><p>show this help message and exit</p></em>
  <p>--websites WEBSITES   </p>
  <em><p>The transaction types at the website you want to perform from the available actions</p></em>
  <p>-l, --list            </p>
  <em><p>List all available actions</p></em>
  <p>-R, --random          </p>
  <em><p>Use wallets in a random order</p></em>

<h4>Wallets:</h4>
  <p>--wallet WALLET       </p>
  <em><p>The wallet you want to use</p></em>
  <p>--wallets WALLETS     </p>
  <em><p>The wallets you want to use</p></em>
<h4>Wait Between Wallets:</h4>
  <p>--wait-between-wallets-max-seconds WAIT_BETWEEN_WALLETS_MAX_SECONDS</p>
                        <em><p>The maximum time in seconds to wait between wallets default: 1800 seconds (30 minutes)</p></em>
  <p>--wait-between-wallets-min-seconds WAIT_BETWEEN_WALLETS_MIN_SECONDS</p>
                        <em><p>The minimum time in seconds to wait between wallets default: 1200 seconds (20 minutes)</p></em>
<h4>Wait Between Websites:</h4>
  <p>--wait-between-websites-max-seconds WAIT_BETWEEN_WEBSITES_MAX_SECONDS</p>
                        <em><p>The maximum time in seconds to wait between websites default: 1200 seconds (20 minutes)</p></em>
  <p>--wait-between-websites-min-seconds WAIT_BETWEEN_WEBSITES_MIN_SECONDS</p>
                        <em><p>The minimum time in seconds to wait between websites default: 300 seconds (5 minutes)</p></em>
<h4>Wait Between Cycles:</h4>
  <p>--wait-between-cycles-max-seconds WAIT_BETWEEN_CYCLES_MAX_SECONDS</p>
                        <em><p>The maximum time in seconds to wait between cycles default: 48600 (12 hours and 90 minutes)</p></em>
  <p>--wait-between-cycles-min-seconds WAIT_BETWEEN_CYCLES_MIN_SECONDS</p>
                        <em><p>The minimum time in seconds to wait between cycles default: 43500 (12 hours and 5 minutes)</p></em>
<h4>Swap Skydrome Settings:</h4>
  <p>--skydrome-from-token SKYDROME_FROM_TOKEN</p>
                        <em><p>The token you want to swap from</p></em>
  <p>--skydrome-to-token SKYDROME_TO_TOKEN</p>
                        <em><p>The token you want to swap to</p></em>
  <p>--skydrome-min-amount SKYDROME_MIN_AMOUNT</p>
                        <em><p>The amount of the token you want to swap</p></em>
  <p>--skydrome-max-amount SKYDROME_MAX_AMOUNT</p>
                        <em><p>The amount of the token you want to swap</p></em>
  <p>--skydrome-decimal SKYDROME_DECIMAL</p>
                        <em><p>The decimal of the token you want to swap</p></em>
  <p>--skydrome-slippage SKYDROME_SLIPPAGE</p>
                        <em><p>The slippage of the token you want to swap</p></em>
  <p>--skydrome-all-amount SKYDROME_ALL_AMOUNT</p>
                        <em><p>Swap all the amount of the token you want to swap</p></em>
  <p>--skydrome-min-percent SKYDROME_MIN_PERCENT</p>
                        <em><p>The minimum percent of the token you want to swap</p></em>
  <p>--skydrome-max-percent SKYDROME_MAX_PERCENT</p>
                        <em><p>The maximum percent of the token you want to swap</p></em>
<p></p>
<h4>Swap Zebra Settings:</h4>
  <p>--zebra-from-token ZEBRA_FROM_TOKEN</p>
                        <em><p>The token you want to swap from</p></em>
  <p>--zebra-to-token ZEBRA_TO_TOKEN</p>
                        <em><p>The token you want to swap to</p></em>
  <p>--zebra-min-amount ZEBRA_MIN_AMOUNT</p>
                        <em><p>The amount of the token you want to swap</p></em>
  <p>--zebra-max-amount ZEBRA_MAX_AMOUNT</p>
                        <em><p>The amount of the token you want to swap</p></em>
  <p>--zebra-decimal ZEBRA_DECIMAL</p>
                        <em><p>The decimal of the token you want to swap</p></em>
  <p>--zebra-slippage ZEBRA_SLIPPAGE</p>
                        <em><p>The slippage of the token you want to swap</p></em>
  <p>--zebra-all-amount ZEBRA_ALL_AMOUNT</p>
                        <em><p>Swap all the amount of the token you want to swap</p></em>
  <p>--zebra-min-percent ZEBRA_MIN_PERCENT</p>
                        <em><p>The minimum percent of the token you want to swap</p></em>
  <p>--zebra-max-percent ZEBRA_MAX_PERCENT</p>
                        <em><p>The maximum percent of the token you want to swap</p></em>
<p></p>
<h4>Swap SyncSwap Settings:</h4>
  <p>--syncswap-from-token SYNCSWAP_FROM_TOKEN</p>
                        <em><p>The token you want to swap from</p></em>
  <p>--syncswap-to-token SYNCSWAP_TO_TOKEN</p>
                        <em><p>The token you want to swap to</p></em>
  <p>--syncswap-min-amount SYNCSWAP_MIN_AMOUNT</p>
                        <em><p>The amount of the token you want to swap</p></em>
  <p>--syncswap-max-amount SYNCSWAP_MAX_AMOUNT</p>
                        <em><p>The amount of the token you want to swap</p></em>
  <p>--syncswap-decimal SYNCSWAP_DECIMAL</p>
                        <em><p>The decimal of the token you want to swap</p></em>
  <p>--syncswap-slippage SYNCSWAP_SLIPPAGE</p>
                        <em><p>The slippage of the token you want to swap</p></em>
  <p>--syncswap-all-amount SYNCSWAP_ALL_AMOUNT</p>
                        <em><p>Swap all the amount of the token you want to swap</p></em>
  <p>--syncswap-min-percent SYNCSWAP_MIN_PERCENT</p>
                        <em><p>The minimum percent of the token you want to swap</p></em>
  <p>--syncswap-max-percent SYNCSWAP_MAX_PERCENT</p>
                        <em><p>The maximum percent of the token you want to swap</p></em>
<p></p>
<h4>Swap XYSwap Settings:</h4>
  <p>--xyswap-from-token XYSWAP_FROM_TOKEN</p>
                        <em><p>The token you want to swap from</p></em>
  <p>--xyswap-to-token XYSWAP_TO_TOKEN</p>
                        <em><p>The token you want to swap to</p></em>
  <p>--xyswap-min-amount XYSWAP_MIN_AMOUNT</p>
                        <em><p>The amount of the token you want to swap</p></em>
  <p>--xyswap-max-amount XYSWAP_MAX_AMOUNT</p>
                        <em><p>The amount of the token you want to swap</p></em>
  <p>--xyswap-decimal XYSWAP_DECIMAL</p>
                        <em><p>The decimal of the token you want to swap</p></em>
  <p>--xyswap-slippage XYSWAP_SLIPPAGE</p>
                        <em><p>The slippage of the token you want to swap</p></em>
  <p>--xyswap-all-amount XYSWAP_ALL_AMOUNT</p>
                        <em><p>Swap all the amount of the token you want to swap</p></em>
  <p>--xyswap-min-percent XYSWAP_MIN_PERCENT</p>
                        <em><p>The minimum percent of the token you want to swap</p></em>
  <p>--xyswap-max-percent XYSWAP_MAX_PERCENT</p>
                        <em><p>The maximum percent of the token you want to swap</p></em>