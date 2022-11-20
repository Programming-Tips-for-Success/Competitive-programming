import pandas as pd
import quandl as q
import numpy as np

q.ApiConfig.api_key = "<API key>”
msft_data = q.get("EOD/MSFT", start_date="2010-01-01", end_date="2019-01-01")
msft_data.head()

msft_data.describe()
msft_data.resample('M').mean()

# assign `Adj Close` to `daily_close`
daily_close = msft_data[['Adj_Close']]
# returns as fractional change
daily_return = daily_close.pct_change()
# replacing NA values with 0

daily_return.fillna(0, inplace=True)
print(daily_return)

mdata = msft_data.resample('M').apply(lambda x: x[-1])

monthly_return = mdata.pct_change()

# assigning adjusted closing prices to 

adj_pricesadj_price = msft_data['Adj_Close']
# calculate the moving average
mav = adj_price.rolling(window=50).mean()
# print the resultprint(mav[-10:])

# import the matplotlib package to see the plot

import matplotlib.pyplot as plt

adj_price.plot()
mav.plot()

# https://www.freecodecamp.org/news/algorithmic-trading-in-python/