import json
import time
import requests
def get_data():
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    api_key = 'H9BZCXCEOBDGG625'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=' + api_key
    r = requests.get(url)
    try:
        data = r.json()
        path = r"C:\Users\yucel\Data_Center\Data Lake/"
        with open(path + "stock_market_raw_data" + "IBM_" + str(time.time()), "w") as outfile:
            json.dump(data, outfile)
    except:
       print("file could not be written")

get_data()