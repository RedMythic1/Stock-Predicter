import finnhub
import math




fh = finnhub.Client(api_key="cakj47iad3ier73m8dtg")
x = fh.quote("AAPL")['c']

y = (3.36805*x) - 281.54
print(y)

