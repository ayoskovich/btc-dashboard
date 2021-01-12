from io import StringIO
from . import helpers


class Dataset():
  """ Class for dataset """
  def __init__(self, n, path, descr):
    """ 
    inputs:
      n (int): Number of records to get
      path (str): Path to datafile
      descr (str): Description of data

    computed:
      data (pd.DataFrame): Raw data
    """
    self.n = n
    self.path = path
    self.descr = descr
    self.data = helpers.read(path, n)



class Future():
  """ Class for the future """

  def __init__(self, nDays, dataset):
    """
    inputs:
      nDays (int): Number of days to forecast
      dataset (Dataset): Dataset object

    computed:
      data (pd.DataFrame): Raw data
    """
    self.nDays = nDays
    self.dataset = dataset
    self.data = dataset.data

  def sma(self, amt):
    """ Simple moving average """
    return self.data.rolling(amt).mean()
 
  def smm(self, amt):
    """ Simple moving median """
    return self.data.rolling(amt).median()

  def ema(self, alpha):
    """ Exponential weighted average """
    return self.data.ewm(alpha=alpha).mean()

  def how_likely(self, scen):
    """ How likely is scen? """
    pass

