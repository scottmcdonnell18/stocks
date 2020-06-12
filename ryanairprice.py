import datetime as dt
from pandas.util.testing import assert_frame_equal
import pandas_datareader.data as web

today = dt.date.today()
lastmonth = today - dt.timedelta(30)

df = web.DataReader('RYAAY', 'yahoo', today)
df2 = web.DataReader('RYAAY', 'yahoo', lastmonth)

todays_price = int(df["Adj Close"][0])
lastmonth = int(df2["Adj Close"][0])

def main():
    print('------------------------------------------------------------')
    print("Today's date is {} and Ryanair's stock price is {:.2f}".format(today, df["Adj Close"][0]))
    print("Low: {:.2f}, High: {:.2f}".format(df["Low"][0], df["High"][0]))
    print("There have been a total of {} Ryanair shares traded today.".format(df["Volume"][0]))
    print("This day last month, its price was {:.2f}".format(df2["Adj Close"][0]))

    if todays_price > lastmonth:
        print('Ryanair stock price has rose by {:.2f} percent in the last 30 days'.format(percent_change(todays_price, lastmonth)))
    elif todays_price < lastmonth:
        print('Ryanair stock price has dropped by {:.2f} percent in the last 30 days'.format(percent_change(todays_price, lastmonth)))
    else:
        print("Ryanir's stock price has remained the same")

def percent_change(todays_price, lastmonth):
    return (todays_price - lastmonth) / lastmonth * 100

if __name__ == '__main__':
    main()
