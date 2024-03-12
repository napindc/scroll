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

1) All setting are a


3) In the rpc.json file at the path zksync/data/rpc.json we can change the rpc to ours

