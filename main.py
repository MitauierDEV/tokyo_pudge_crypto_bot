import requests
CRYPTO_CURRENCY_URL = 'https://api.coingecko.com/api/v3/simple/price';

def get_crypto_currency_price(currency):
  price = requests.get(CRYPTO_CURRENCY_URL, params={
    "ids": currency,
    "vs_currencies": "usd"
  })
  return price

def main():
    price = get_crypto_currency_price('bitcoin')
    print(price.text)


if __name__ == "__main__":
    main()
