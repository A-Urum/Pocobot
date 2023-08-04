import json
import requests
from Config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Валюта "{base}" переводится в валюту "{base}" по цене 1 к 1.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось найти валюту "{quote}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось найти валюту "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не верно указан параметр <колличество переводимой валюты> - "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base


