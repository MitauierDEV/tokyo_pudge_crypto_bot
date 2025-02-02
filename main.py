from crypto_client.crypto_currency_client import *

def main():
    price = get_crypto_currency_price_by_date('bitcoin', '29-12-2024')
    print(price.text)


if __name__ == "__main__":
    main()
