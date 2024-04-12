## Description

This pull request introduces significant enhancements to the existing functionality, enabling automated trades across multiple websites using a single Python command. The key features include:

Unified Command: Users can now execute automated trades across multiple websites with a single Python command.

Support for Multiple Wallets: The system now accepts one or multiple wallet private keys for performing swaps, offering enhanced flexibility to users.

Dynamic Randomization Schedule: Trades are executed using a dynamically randomizing schedule, contributing to improved security and efficiency.

Configurability: Command-line arguments have been exposed to facilitate easy configuration, allowing users to customize randomization schedules, swap amounts, and tokens.

Cycle Functionality: The system automatically cycles between swapping from ETH to USDC and back, optimizing trading processes.

## Changes Made
Implemented run_swaps.py to enable executing automated trades across multiple websites.

Added support for accepting one or multiple wallet private keys for performing swaps.

Integrated dynamic randomization schedule for executing trades and recycling wallets.

Exposed command-line arguments for configuring randomization schedules, swap amounts, and tokens.

Implemented automatic cycling between swapping from ETH to USDC and back for optimized trading.

## Usage
python run_swaps.py --wallets "WALLET_KEY1 WALLET_KEY2 ... WALLET_KEYN"
or
python run_swaps.py --wallet_file <file_name.json>

## Testing
Manual testing has been conducted to validate the behavior across different machines all using one wallet.

## Additional Notes
Documentation has been updated to reflect the changes and provide guidance on usage.

All new code adheres to best practices.
