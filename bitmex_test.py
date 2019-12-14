import bitmex
from settings import *
import requests
from time import sleep

symbol = 'XBTUSD'
price = 0
# NOT DEMO
client = bitmex.bitmex(test=False, api_key=key, api_secret=secret_key)


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


def get_trades(interval, limit, startTime, endTime):
    trades = client.Trade.Trade_getBucketed(
        binSize=interval,
        partial=False,
        symbol=symbol,
        count=limit,
        reverse=False,
        startTime=startTime,
        endTime=endTime
    ).result()
    return trades[0] or []


def new_limit_order(Side, price, amountToTrade):
    client.Order.Order_new(   # limit
        symbol=symbol,
        side=Side,
        orderQty=amountToTrade,
        price=priceNow,       # Need to check this variable
        ordType='Limit'
        ).result()


def new_stop_order(Side, price, amountToTrade):
    client.Order.Order_new(   # stop
        symbol=symbol,   # 'XBTUSD'
        side=Side,
        orderQty=amountToTrade,
        stopPx=price,
        ordType='Stop',
        execInst='LastPrice'
        ).result()


def new_close_order(Side, price, amountToTrade):
    client.Order.Order_new(
        symbol=symbol,
        side=Side,
        orderQty=amountToTrade,
        price=price,
        execInst='ReduceOnly'
        ).result()
