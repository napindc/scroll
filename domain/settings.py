
# GWEI CONTROL MODE
CHECK_GWEI = False  # True/False
MAX_GWEI = 20

MAX_PRIORITY_FEE = {
    "ethereum": 0.01,
    "polygon": 40,
    "arbitrum": 0.1,
    "base": 0.1,
    "zksync": 0.25,
}

GAS_MULTIPLIER = 1.3

# RETRY MODE
RETRY_COUNT = 3

LAYERSWAP_API_KEY = ""
# To manage wait between wallets or cycles
managingEnvironment = {
    "development": {
        "waitTimeBetweenSwapBack": {"from": 40, "to": 60},
        "waitTimeBetweenWallets": {"from": 60, "to": 80},
        "waitBetweenCycles": {"from": 60, "to": 80},
    },
    "production": {
        "waitTimeBetweenSwapBack": {"from": 120, "to": 300},
        "waitTimeBetweenWallets": {"from": 120, "to": 300},
        "waitBetweenCycles":  {"from": ((12*60*60)+5), "to": (12*60*60)+90},
    },
    "totalSecond":3600,
    "totalMinutes":60,
    "python_running_env": "production",
}



