from flask import Flask
from flask import jsonify
import requests
import json
import pandas as pd

from dash.forecast import Dataset, Future

app = Flask(__name__)


@app.route('/')
def hello():
  return jsonify({'message':'hello'})


@app.route('/data/<amt>')
def sma(amt):
  """ Simple moving average of length dur """
  A = Dataset(int(amt), '../prices.txt', 'Short history')
  f1 = Future(3, A)

  return f1.data.to_html()

@app.route('/shout/<tar>')
@app.route('/shout/')
def yell(tar=None):
  """ Yell if price moves above tar """
  load = {
    'tar': tar
  }

  return jsonify(load)

