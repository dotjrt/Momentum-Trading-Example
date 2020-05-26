"""The config variables for the trading algo."""
import alpaca_trade_api as tradeapi
import os


REST_CXN = tradeapi.REST(
    base_url=os.environ.get(PAPER_API_ENDPOINT),
    key_id=os.environ.get(PAPER_API_KEY_ID),
    secret_key=os.environ.get(PAPER_API_SECRET_KEY)
)

STREAMING_CXN = tradeapi.StreamConn(
    base_url=os.environ.get(PAPER_API_ENDPOINT),
    key_id=os.environ.get(PAPER_API_KEY_ID),
    secret_key=os.environ.get(PAPER_API_SECRET_KEY)
)

"""Trading strategy parameters."""
# We only consider stocks with per-share prices inside this range
MIN_SHARE_PRICE = 2.0
MAX_SHARE_PRICE = 16.0  # Was 13.0
# Minimum previous-day dollar volume for a stock we might consider
MIN_LAST_DV = 500000
# Stop limit to default to
DEFAULT_STOP = 0.90  # Was .95
# How much of our portfolio to allocate to any one position
RISK = 0.001
# Percentage increase in stock price we're looking for
TODAYS_CHANGE_PCT = 3.0  # Was 3.5
# Time, in minutes, to wait after market opens before trading
WAIT = 15
