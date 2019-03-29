from settings import *
from dl_data import *
from bitmex_test import *
import requests, json
from time import sleep
from collections import defaultdict


s1 = s2 = r1 = r2 = 0
target = 0

def read_raw_data(timeframe, limit_n):
    datetime_interval = timeframe
    limit = limit_n
    td = get_trades(datetime_interval, limit)   # Эта хрень почему-то возвращает tuple...

    for j in range(len(td[0])):                 # Это для преобразования tuple в словарь, надо допилить, чтобы возвращал все строки!!
        ti = dict(td[0][j])
        df = {}
        df.update(ti)

    df = convert_to_dataframe(df)
    df = StockDataFrame.retype(df)
    print(df)
    return df                                   # Сейчас функция возвращает только одну строку (датафрейм, содержащий одну строку)


def bot_init():
    df = read_raw_data('1h', 24)
    df['atr'] = df.get('atr')           #calculate RSI
    if (df['atr'][24] > 20):
        s1 = min(df['low'] - 30)        # set support level
        r1 = max(df['high'] + 30)
    else:
        s1 = min(df['low'] - 20)        #set support level
        r1 = max(df['high'] + 20)       #set resistance level
    print(df['atr'])
    #return df
    #    print('Available balance: ', margin)



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
#sleep(3)
#td = read_raw_data('1m', 5)
#td = get_trades('1m', 5)


#while True:
    #bot_run()