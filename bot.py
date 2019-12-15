from dl_data import convert_to_dataframe
from bitmex_test import get_trades, get_balance, new_limit_order, new_stop_order
from time import sleep
from stockstats import StockDataFrame
from datetime import datetime, timedelta


def read_raw_data(time_frame: str, limit_n: int, startTime: datetime, endTime: datetime):
    _trades = get_trades(time_frame, limit_n, startTime, endTime)
    _data_frame = convert_to_dataframe(_trades)
    _result = StockDataFrame.retype(_data_frame)
    return _result


def bot_init():
    time_now = datetime.now()
    start_time = time_now - timedelta(hours=24)
    margin, marginPcnt = get_balance()
    margin *= 100
    marginPcnt *= 100
    df = read_raw_data('1h', 24, start_time, time_now)
    df['atr'] = df.get('atr')           # calculate RSI
    if df['atr'][23] > 20:              # if atr > 20, set s/r for high volatility
        s1 = min(df['low'] - 30)        # set support level
        r1 = max(df['high'] + 30)       # set resistance level
    else:
        s1 = min(df['low'] - 20)        # set support level
        r1 = max(df['high'] + 20)       # set resistance level

    print(df)
    print('Available balance: ', margin)
    print('Percentage of your margin used is: ' + str(marginPcnt) + '%')
    return df


def bot_run():
    time_now = datetime.now()
    start_time = time_now - timedelta(minutes=10)
    margin, marginPcnt = get_balance()
    marginPcnt *= 100
    # pos = margin * 0.03          # size of current position, not used right now

    df = read_raw_data('1m', 10, start_time, time_now)
    df['macd'] = df.get('macd')     # calculate MACD
    df['macds'] = df.get('macds')   # MACD signal
    df['macdh'] = df.get('macdh')   # MACD histogram
    df['rsi'] = df.get('rsi_15')    # calculate RSI
    df['middle'] = df.get('middle') # get middle price
    print('Last RSI value: ', '{0:.2f}'.format(df['rsi'][9]))           # use format to display 2 decimal places
    print('Last middle price: ', '{0:.2f}'.format(df['middle'][9]))     # use format to display 2 decimal places


''' Simple strategy to be tested and implemented. Not used right now.

    if df['rsi'][20] < 50 and df['macd'][20] > df['macds'][20] and marginPcnt <= 15:
        new_limit_order('Buy', df[60]+1, pos)
        new_stop_order('Sell', df[60]-20, pos)
        total_pos += pos

    elif df['rsi'][20] > 50 and df['macd'][20] < df['macds'][20] and marginPcnt <= 15:
        new_limit_order('Sell', df[60] - 1, pos)
        new_stop_order('Buy', df[60] + 20, pos)
        total_pos += pos
    sleep(1)
'''

bot_init()

while True:
    bot_run()
    sleep(60)
