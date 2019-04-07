from redux_store import *
from dl_data import convert_to_dataframe
from bitmex_test import get_trades, get_balance, new_limit_order, new_stop_order
from time import sleep
from stockstats import StockDataFrame
from datetime import datetime, timedelta


target = 0

def read_raw_data(time_frame: str, limit_n: int, startTime: datetime, endTime: datetime):
    _trades = get_trades(time_frame, limit_n, startTime, endTime)
    _data_frame = convert_to_dataframe(_trades)
    _result = StockDataFrame.retype(_data_frame)
    return _result


def bot_init():
    time_now = datetime.now()
    start_time = time_now - timedelta(hours=24)
    df = read_raw_data('1h', 24, start_time, time_now)
    df['atr'] = df.get('atr')           # calculate RSI
    if df['atr'][23] > 20:
        s1 = min(df['low'] - 30)       # set support level
        r1 = max(df['high'] + 30)
        #app_reducer_sr(state, 'SET_S1')
    else:
        s1 = min(df['low'] - 20)        # set support level
        r1 = max(df['high'] + 20)       # set resistance level
    store.dispatch(({'type': 'SET_S1', 'support_1': s1}))
    print (s1)

    print (df)
    print(df['atr'])
    # return df
    # print('Available balance: ', margin)


def bot_run():
    margin, marginPcnt = get_balance()
    marginPcnt *= 100
    pos = margin * 0.03
    print(marginPcnt)

    df = read_raw_data('minute', 20)
    df['macd'] = df.get('macd')    # calculate MACD
    df['macds'] = df.get('macds')  # MACD signal
    df['macdh'] = df.get('macdh')  # MACD histogram
    df['rsi'] = df.get('rsi_15')   # calculate RSI
    print(['rsi'])

    if df['rsi'][20] < 50 and df['macd'][20] > df['macds'][20] and marginPcnt <= 15:
        new_limit_order('Buy', df[60]+1, pos)
        new_stop_order('Sell', df[60]-20, pos)
        total_pos += pos

    elif df['rsi'][20] > 50 and df['macd'][20] < df['macds'][20] and marginPcnt <= 15:
        new_limit_order('Sell', df[60] - 1, pos)
        new_stop_order('Buy', df[60] + 20, pos)
        total_pos += pos
    sleep(1)


bot_init()
# sleep(3)
# td = read_raw_data('1m', 5)
# td = get_trades('1m', 5)


# while True:
#     bot_run()
