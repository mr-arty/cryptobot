import bitmex
from settings import *
import requests, json
from time import sleep

symbol = 'XBTUSD'
Side = 'Sell'
amountToTrade = 50
price = 3912


client = bitmex.bitmex(
    test = False, #НЕ демо версия
    api_key = key,
    api_secret = secret_key,
    )

#balance = client.User.User_getMargin(
#    currency='XBt'
#    ).result()[0]['walletBalance']
'''
prices = client.Order.Order_bookGetL2(
    symbol=symbol,
    depth=10
#    count = 100, # float | Number of results to fetch. (optional) (default to 100)
#    start = 0, # float | Starting point for results. (optional) (default to 0)
#    reverse = False, # bool | If true, will sort results newest first. (optional) (default to false)
#    start_time = '2019-03-01T19:20:30+01:00', # datetime | Starting date filter for results. (optional)
#    end_time = '2019-03-10T19:20:30+01:00' # datetime | Ending date filter for results. (optional)
    ).result()[0]

for price in prices:
    closes = price['close']
'''
'''
client.Order.Order_new( #limit
    symbol = symbol,
    side = Side,
    orderQty = amountToTrade,
    price = priceNow, #Need to check this variable
    ordType='Limit'
    ).result()

client.Order.Order_new( #stop
    symbol = symbol, # 'XBTUSD'
    side = Side,
    orderQty = amountToTrade,
    stopPx = price,
    ordType = 'Stop',
    execInst = 'LastPrice'
    ).result()


client.Order.Order_new(
    symbol = symbol,
    side = Side,
    orderQty = amountToTrade,
    price = price,
    execInst = 'ReduceOnly'
    ).result()
'''
for n in range(50):
    response = requests.get("https://www.bitmex.com/api/v1/orderBook/L2?symbol=xbt&depth=1").json()
    ether_ask_price = response[0]['price']
    ether_bid_price = response[1]['price']
    print(ether_ask_price, ether_bid_price)
    sleep(2)

#print(balance / 1e8)
