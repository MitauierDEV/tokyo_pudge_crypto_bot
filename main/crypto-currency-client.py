import requests

CRYPTO_CURRENCY_URL = 'https://api.coingecko.com/api/v3/simple/price';

def get_crypto_currency_price(currency):
  price = requests.get(CRYPTO_CURRENCY_URL, params={
    "ids": currency,
    "vs_currencies": "usd"
  })
  return price




# BTC -> get_crypto_currency_current_price(BTC) -> API crypto -> 100000

# domen: .com .ru .de
# host https://trello.rer.com
# URL https://trello.rer.com/b/3zh8w1d1/our-pet-project
