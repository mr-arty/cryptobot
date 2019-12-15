## Crypto-exchange query bot

This bot connects to the Bitmex exchange using its REST API. The settins.py file should contain a key and a secret key.

The bot uses the stockstats library https://github.com/jealous/stockstats which contains many useful trading indicators.

When initialized, bot prints out a table with prices for the last 24 hours and ATR (Average True Range). The ATR value
is used to calculate Support and Resistance levels. When the bot is running it prints out the RSI value and the last
middle price: middle = (close + high + low) / 3 . The values are refreshed every 60 seconds. The bitmex_test module 
contains methods to place different kinds of orders (limit, stop and close). The trading pair (XBTUSD) is also 
hard-coded in this module. Feel free to use them and implement your own strategy. I gave an example strategy in bot.py 
but it has not been tested and is not guaranteed to work.