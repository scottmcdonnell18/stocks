import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2020, 4, 1)
end = dt.datetime(2020, 5, 31)

df = web.DataReader('RYAAY', 'yahoo', start, end)
print(df.tail(6))