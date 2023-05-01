import finnhub


fh = finnhub.Client(api_key="cakj47iad3ier73m8dtg")
AAPL = fh.quote("AAPL")
NVDA = fh.quote("NVDA")


AAPL_GAIN = AAPL['c'] - AAPL['pc']
NVDA_EST_CLOSE = round((3.36805*AAPL['c'])-281.54,2)

NVDA_ACT_CLOSE = round(NVDA['c'],2)

NVDA_CLOSE_DEV = round(NVDA_EST_CLOSE/NVDA_ACT_CLOSE,4)
print(NVDA_EST_CLOSE,NVDA_ACT_CLOSE, NVDA_CLOSE_DEV)
