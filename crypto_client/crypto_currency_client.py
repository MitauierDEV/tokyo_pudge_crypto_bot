import requests

CRYPTO_CURRENCY_URL = 'https://api.coingecko.com'

def get_crypto_currency_price_by_date(currency, date):
  price = requests.get(CRYPTO_CURRENCY_URL + f'/api/v3/coins/{currency}/history', params={
    "date": date
  })
  return price

def get_crypto_currency_price(currency):
  price = requests.get(CRYPTO_CURRENCY_URL + '/api/v3/simple/price', params={
    "ids": currency,
    "vs_currencies": "usd"
  })
  return price

def get_crypto_currency_list():
  price = requests.get(CRYPTO_CURRENCY_URL + '/api/v3/coins/list')
  return price
