from flask import Flask
from flask import jsonify
import requests
import json
import pandas as pd


app = Flask(__name__)


def last_price():
  """ Get the latest price """

  with open('../prices.txt', 'r') as f:
    last_line = f.readlines()[-1]
    price = float(last_line.split(',')[0])

  return price


@app.route('/')
def hello():
  return jsonify({'message':'hello'})


@app.route('/shout/<tar>')
@app.route('/shout/')
def yell(tar=None):
  """ Yell if price moves above tar """
  load = {
    'tar': tar
  }

  return jsonify(load)

