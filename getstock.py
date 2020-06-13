import sys
import datetime as dt
import pandas as pd
import pandas_datareader.data as web

try:
    stock = sys.argv[1]
    today = dt.date.today()
    df = web.DataReader(stock, 'yahoo', today)
    print("Today's price: {:.2f}".format(df['Adj Close'][0]))

except IndexError:
    print('You must enter a stock to check its price!')
    print('e.g RYAAY or TSLA')
