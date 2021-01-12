"""
Helper functions
"""

import pandas as pd


def read(path, number):
  """ Read in historic bitcoin data 
  
  path (str): Path to file
  number (int): Number of records to read 
    from the bottom of the file
  """
  with open(path, 'r') as f:
    lines = f.readlines()[-number:]

  prices = [x.split(',')[0] for x in lines]
  times  = [x.split(',')[1] for x in lines]
  times =  [x.replace('\n', '') for x in times]

  frame = pd.DataFrame({
    'price':prices,
    'time':times
  })

  frame['price'] = frame['price'].astype(float)

  return frame


