import pandas as pd
import requests
from stockstats import StockDataFrame
from datetime import datetime

from_symbol = 'XBTUSD'
to_symbol = 'USD'
limit = 180             #180 minutes (3 hours)
exchange = 'Bitmex'     #'Bitmex'
datetime_interval = 'minute'

def get_filename(from_symbol, to_symbol, exchange, datetime_interval, download_date):
    return '%s_%s_%s_%s_%s.csv' % (from_symbol, to_symbol, exchange, datetime_interval, download_date)

'''
def download_data(from_symbol, to_symbol, exchange, datetime_interval, limit):
    supported_intervals = {'minute', 'hour', 'day'}
    assert datetime_interval in supported_intervals,\
        'datetime_interval should be one of %s' % supported_intervals

    print('Downloading %s trading data for %s %s from %s' %
          (datetime_interval, from_symbol, to_symbol, exchange))
    base_url = 'https://min-api.cryptocompare.com/data/histo'
    url = '%s%s' % (base_url, datetime_interval)

    params = {'fsym': from_symbol, 'tsym': to_symbol,
              'limit': limit, 'aggregate': 1,
              'e': exchange}
    request = requests.get(url, params=params)
    data = request.json()
    return data
'''

def convert_to_dataframe(data):
    df = pd.io.json.json_normalize(data)
    #df['timestamp'] = pd.to_datetime(df.time, unit='s')
    df = df[['timestamp', 'low', 'high', 'open',
         'close', 'volume']]
    return df


def filter_empty_datapoints(df):
    indices = df[df.sum(axis=1) == 0].index
    print('Filtering %d empty datapoints' % indices.shape[0])
    df = df.drop(indices)
    return df
'''
data = download_data(from_symbol, to_symbol, exchange, datetime_interval, limit)
df = convert_to_dataframe(data)
df = filter_empty_datapoints(df)

df = StockDataFrame.retype(df)
df['macd'] = df.get('macd') # calculate MACD
df['rsi'] = df.get('rsi_15') #calculate RSI

print(df)


current_datetime = datetime.now().date().isoformat()
filename = get_filename(from_symbol, to_symbol, exchange, datetime_interval, current_datetime)
print('Saving data to %s' % filename)
df.to_csv(filename, index=False)
'''