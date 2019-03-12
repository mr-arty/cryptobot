#import pandas as pd
from stockstats import StockDataFrame
from dl_data import *

#filename = 'BTC_USD_Bitstamp_hour_2019-03-10.csv'

def read_dataset(filename):
    print('Reading data from %s' % filename)
    df = pd.read_csv(filename)
    df.datetime = pd.to_datetime(df.datetime) # change type from object to datetime
    df = df.set_index('datetime')
    df = df.sort_index() # sort by datetime
    print(df.shape)
    return df

#df = read_dataset(filename)


df = StockDataFrame.retype(df)
df['macd'] = df.get('macd') # calculate MACD
df['rsi'] = df.get('rsi_15') #calculate RSI

print(df)
print('MACD: ', df['macd'][180], '\nMACD SIGNAL: ', df['macds'][180], '\nMACD HISTO: ', df['macdh'][180])
print('RSI: ', df['rsi'][180])