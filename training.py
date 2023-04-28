import finnhub
import math

def calculate_y(x1, y1, a, b, h, j, k):
    numerator = j * (a * math.pow(b, x1 - h) + k) ** x1
    denominator = (a * x1 + k) ** y1
    return numerator / denominator


fh = finnhub.Client(api_key="cakj47iad3ier73m8dtg")
x = fh.quote("AAPL")['c']

y = (-.00000180476*(x**5))+(.00105509*(x**4))+(-.230267*(x**3))+(22.2391*(x**2))+(-800.969*x)
num = 0
while num<=10000:
    y = calculate_y(x,y,-.0000128807,.453797,97.674,112.788,.996966)
    num+=1
print(y)
