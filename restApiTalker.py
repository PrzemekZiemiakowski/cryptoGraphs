import json
import requests
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import apikey
# from requests import Request, Session
##GET
#​/tickers
#Price
# Press the green button in the gutter to run the script.

headers = {
    'X-CMC_PRO_API_KEY': 'f14d06bc-09cf-4557-89cd-2d8f3fbb9db4',
    'Accepts': 'application/json'
}
params = {
    'start': '1',
    'limit': '10',
    'convert': 'USD'
}
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
def readData():
    json= requests.get(url, params=params, headers=headers).json()
    return json

    print(json)
    coins =json['data']
    data_list=[]
    for x in coins:
        name=x['slug']
        actPrice=x['quote']['USD']['price']
        volume=x['quote']['USD']['volume_24h']
        print("name= ",name,"cena= ",actPrice,"volume= ",volume)
        volumeDesc="A measure of how much of a cryptocurrency was traded in the last 24 hours"
        actPriceDesc=""