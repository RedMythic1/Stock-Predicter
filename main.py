import finnhub


fh = finnhub.Client(api_key="cakj47iad3ier73m8dtg")
AAPL = fh.quote("AAPL")
NVDA = fh.quote("NVDA")

AAPL_GAIN = AAPL['c'] - AAPL['pc']
NVDA_EST_CLOSE = round(-38.6718*((1)**((AAPL['c']**6)-20900000000000))+314.034,2)

NVDA_ACT_CLOSE = round(NVDA['c'],2)

NVDA_CLOSE_DEV = round(NVDA_EST_CLOSE/NVDA_ACT_CLOSE,2)
print(NVDA_EST_CLOSE,NVDA_ACT_CLOSE, NVDA_CLOSE_DEV)