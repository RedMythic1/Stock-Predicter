import finnhub
fh = finnhub.Client(api_key="cakj47iad3ier73m8dtg")
BTC = fh.quote("BTC-USD")
NVDA = fh.quote("NVDA")

BTC_GAIN = BTC['c'] - BTC['o']
NVDA_EST_GAIN = BTC_GAIN*(93/1000)
