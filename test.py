from dash.forecast import Dataset, Future

A = Dataset(25, '../prices.txt', 'Short history')
B = Dataset(100, '../prices.txt', 'Long history')

f1 = Future(3, A)
f2 = Future(3, B)

df = f1.data
