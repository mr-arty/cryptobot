import pandas

from_symbol = 'XBTUSD'
to_symbol = 'USD'
limit = 180             # 180 minutes (3 hours)
exchange = 'Bitmex'     # 'Bitmex'
datetime_interval = 'minute'


def get_filename(from_symbol, to_symbol, exchange, datetime_interval, download_date):
    return '%s_%s_%s_%s_%s.csv' % (from_symbol, to_symbol, exchange, datetime_interval, download_date)


def convert_to_dataframe(data):
    df = pandas.io.json.json_normalize(data)
    df = df[['timestamp', 'low', 'high', 'open', 'close', 'volume']]
    return df


def filter_empty_datapoints(df):
    indices = df[df.sum(axis=1) == 0].index
    print('Filtering %d empty datapoints' % indices.shape[0])
    df = df.drop(indices)
    return df
