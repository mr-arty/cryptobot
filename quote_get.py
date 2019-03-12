from __future__ import print_function
import time
from bitmex_test import *
import bitmex_client
from bitmex_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
#api_key_id = key # str | API Key ID (public component).
#bitmex_client.configuration.api_key['api-key'] = secret_key

api_instance = bitmex_client.QuoteApi()
#symbol = 'symbol_example' # str | Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.  You can also send a timeframe, e.g. `XBU:monthly`. Timeframes are `daily`, `weekly`, `monthly`, `quarterly`, and `biquarterly`. (optional)
#filter = 'filter_example' # str | Generic table filter. Send JSON key/value pairs, such as `{\"key\": \"value\"}`. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#Timestamp-Filters) for more details. (optional)
#columns = 'columns_example' # str | Array of column names to fetch. If omitted, will return all columns.  Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect. (optional)
count = 100 # float | Number of results to fetch. (optional) (default to 100)
start = 0 # float | Starting point for results. (optional) (default to 0)
reverse = False # bool | If true, will sort results newest first. (optional) (default to false)
start_time = '2019-03-01T19:20:30+01:00' # datetime | Starting date filter for results. (optional)
end_time = '2019-03-10T19:20:30+01:00' # datetime | Ending date filter for results. (optional)

try:
    # Get Quotes.
    api_response = api_instance.quote_get(symbol=symbol, count=count, start=start, reverse=reverse, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteApi->quote_get: %s\n" % e)