from io import StringIO
from . import helpers


class Dataset():
  """ Class for dataset """
  def __init__(self, n, path, descr):
    self.n = n
    self.path = path
    self.descr = descr
    self.data = helpers.read(path, n)



class Future():
  """ Class for the future """

  def __init__(self, nDays):
    self.nDays = nDays


  def sma(self, amt):
    """ Forecast by using the how method """
    pass

 
  def ema(self, amt):
    pass


  def how_likely(self, scen):
    """ How likely is scen? """
    pass

