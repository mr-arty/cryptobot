import pandas

from_symbol = 'XBTUSD'
to_symbol = 'USD'
limit = 180             # 180 minutes (3 hours)
exchange = 'Bitmex'     # 'Bitmex'
datetime_interval = 'minute'


def convert_to_dataframe(data):
    pandas.set_option('mode.chained_assignment', None)
    df = pandas.io.json.json_normalize(data)
    df = df[['timestamp', 'low', 'high', 'open', 'close', 'volume']]
    return df


def filter_empty_datapoints(df):
    indices = df[df.sum(axis=1) == 0].index
    print('Filtering %d empty datapoints' % indices.shape[0])
    df = df.drop(indices)
    return df
