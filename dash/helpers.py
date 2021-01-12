"""
Helper functions
"""

import pandas as pd

def read(path, number):
  """ Read in the txt file """
  with open(path, 'r') as f:
    lines = f.readlines()[-number:]

  prices = [x.split(',')[0] for x in lines]
  times  = [x.split(',')[1] for x in lines]
  times = [x.replace('\n', '') for x in times]

  frame = pd.DataFrame({
    'price':prices,
    'time':times
  })

  return frame

