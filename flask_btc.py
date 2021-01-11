from flask import Flask
from flask import jsonify
import requests
import json
import numpy as np
import pandas as pd
from datetime import datetime

app = Flask(__name__)

TRADES = [
    (31747.53, 0.00157499),
    (31452.98, 0.00158981)
]
buys = [x[0] for x in TRADES]
amts = [x[1] for x in TRADES]


def last_price():
  ''' Gets the latest price '''

  with open('../prices.txt', 'r') as f:
    last_line = f.readlines()[-1]
    price = float(last_line.split(',')[0])

  return price


@app.route('/gainz')
def get_gainz():

  price = last_price()

  try:
    gainz = np.sum(
        np.array(amts)*(price - np.array(buys))
    )
    gainz = format(gainz, '.2f')

    load = {
      'current_price': price,
      'gainz': gainz
    }

    return jsonify(load)

  except KeyError:
    return jsonify({'error': 'Something went wrong...'})


@app.route('/shout/<tar>')
def yell(tar):
  """ Yell if price moves above tar """
  price = str(last_price())

  load = {
    'last_price': price,
    'message':    price > tar
  }

  # <meta http-equiv="refresh" content="5">
  return f"""
  Current price: {price} 
  <audio controls>
    <source src="up.mp3" type="audio/mpeg">
  </audio>
  """

@app.route('/view')
def show():
  df = pd.read_csv('../prices.txt', names=['price', 'time'])
  return df.to_html()
