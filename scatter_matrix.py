# Getting the data

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
from pandas.plotting import scatter_matrix

yf.pdr_override()

tickers = ['IWM', '^GSPC', 'QQQ', 'AAPL']
startdate = '2020-01-01'
enddate = '2023-03-08'

data = pdr.get_data_yahoo(tickers, start=startdate, end=enddate)['Adj Close']

# Returns

returns = data.pct_change()[1:]
returns.corr()['IWM'].sort_values(ascending=False)

# Graph

scatter_matrix(returns, figsize=(15,6), alpha=0.3)
plt.show()