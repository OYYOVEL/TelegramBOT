import json
import requests
from conf import *


class ExchangeException (Exception):
    pass


class Exchange:
    @staticmethod
    def get_price (quote: str, base: str, amount: str):
        
        try:
            quote_ticker = keys [quote]
            
        except KeyError:
            raise ExchangeException (f'Не смог распознать валюту {quote}')

        try:
            base_ticker = keys [base]
            
        except KeyError:
            raise ExchangeException (f'Не смог распознать валюту {base}')

        try:
            amount = float (amount)
            
        except ValueError:
            raise ExchangeException (f'Не смог распознать количество {amount}')

        r = requests.get (f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        
        total_base = float(json.loads (r.content)[keys [base]])
        
        if base_ticker == 'BTC':
            result = f'{(total_base * amount):.8f}'
            result = result.rstrip('0').rstrip('.') if '.' in result else result
        else:
            result = f'{(total_base * amount):.2f}'
            
        return result
