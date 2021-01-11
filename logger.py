import requests
import time
from datetime import datetime

CREDITS = 10
COST = .005
REQUEST_LIMIT = 10 / .005
SID = 60*60*24

# In seconds
ALLOW_RATE = SID / REQUEST_LIMIT + 3

def get_price():
  URL = 'https://api.cryptowat.ch/markets/kraken/btcusd/price'

  try:
    r = requests.get(URL).json()
    price = format(r['result']['price'], '.2f')
  except:
    price = "Something went wrong"

  rec = f'{price},{datetime.now()}\n'

  return rec

while True:
  with open('prices.txt', 'a') as f:
    f.write(get_price())
    time.sleep(ALLOW_RATE)
