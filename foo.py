from flask import Flask
from flask import jsonify
from datetime import datetime
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/data')
def get_all():
  df = pd.read_csv('prices.txt', names=['price', 'time'])
  return df.to_json(orient='records')

@app.route('/view')
def show():
  df = pd.read_csv('prices.txt', names=['price', 'time'])
  return df.to_html()
