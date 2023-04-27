import finnhub
fh = finnhub.Client(api_key="cakj47iad3ier73m8dtg")
BTC = fh.quote("BTC-USD")
NVDA = fh.quote("NVDA")

BTC_GAIN = BTC['c'] - BTC['pc']
NVDA_EST_GAIN = round(BTC_GAIN*(93/10000),2)
NVDA_EST_CLOSE = round(BTC['c']*(93/10000),2)

NVDA_ACT_CLOSE = round(NVDA['c'],2)
NVDA_ACT_GAIN = round(NVDA['c'] - NVDA['pc'],2)

NVDA_GAIN_DEV = round(NVDA_EST_GAIN/NVDA_ACT_GAIN,2)
NVDA_CLOSE_DEV = round(NVDA_EST_CLOSE/NVDA_ACT_CLOSE,2)
print(NVDA_EST_CLOSE,NVDA_EST_GAIN,NVDA_ACT_CLOSE,NVDA_ACT_GAIN, NVDA_CLOSE_DEV, NVDA_GAIN_DEV)