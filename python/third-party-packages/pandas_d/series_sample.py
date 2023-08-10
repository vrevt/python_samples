import pandas as pd

my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(my_series2['f'])

my_series2[['a', 'b', 'f']] = 123
print(my_series2[['a', 'b', 'f']])