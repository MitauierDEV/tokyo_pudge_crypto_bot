from crypto_client.crypto_currency_client import get_crypto_currency_price

def main():
    price = get_crypto_currency_price('bitcoin')
    print(price.text)


if __name__ == "__main__":
    main()
