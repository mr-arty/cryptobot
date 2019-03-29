import bitmex
from settings import *
import requests, json
from time import sleep

symbol = 'XBTUSD'
'''
Side = 'Sell'
amountToTrade = 50
price = 3912
'''

client = bitmex.bitmex(
    test = False, #НЕ демо версия
    api_key = key,
    api_secret = secret_key,
    )

def get_balance():
    balance = client.User.User_getMargin(
        currency='XBt'
        ).result()[0]['walletBalance']
    balance /= 1e8

    sleep(2)
    marginPcnt = client.User.User_getMargin(
        currency='XBt'
    ).result()[0]['marginUsedPcnt']
    return balance, marginPcnt

def get_trades(interval, limit):
    trades = client.Trade.Trade_getBucketed(
        binSize = interval,
        partial = False,
        symbol = symbol,
        count = limit,
        reverse = False
    ).result()
    return trades

def new_limit_order(Side, price, amountToTrade):
    client.Order.Order_new( #limit
        symbol = symbol,
        side = Side,
        orderQty = amountToTrade,
        price = priceNow, #Need to check this variable
        ordType='Limit'
        ).result()

def new_stop_order(Side, price, amountToTrade):
    client.Order.Order_new( #stop
        symbol = symbol, # 'XBTUSD'
        side = Side,
        orderQty = amountToTrade,
        stopPx = price,
        ordType = 'Stop',
        execInst = 'LastPrice'
        ).result()

def new_close_order(Side, price, amountToTrade):
    client.Order.Order_new(
        symbol = symbol,
        side = Side,
        orderQty = amountToTrade,
        price = price,
        execInst = 'ReduceOnly'
        ).result()


def get_trades_request(interval, limit):        # Нужно допилить эту функцию, чтобы передавать параметры через payload
    trades = requests.get("https://www.bitmex.com/api/v1/trade/bucketed?binSize=1h&symbol=XBTUSD&count=24").json()
    return trades

'''
for n in range(50):
    response = requests.get("https://www.bitmex.com/api/v1/orderBook/L2?symbol=xbt&depth=1").json()
    ether_ask_price = response[0]['price']
    ether_bid_price = response[1]['price']
    print(ether_ask_price, ether_bid_price)
    sleep(2)
'''
#print(balance / 1e8)
