import requests as r
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os


class Price(object):
    PROTOCOL = "https://"
    URL = "pro-api.coinmarketcap.com"
    PATH = "/v1/cryptocurrency/quotes/latest"
    SECRET_KEY = os.environ.get("CMC_SECRET")
    SYMBOL = "XLM"
    
    def main(self):
        parameters = {
          "symbol": self.SYMBOL
        }
        headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': self.SECRET_KEY,
        }

        session = Session()
        session.headers.update(headers)

        try:
          response = session.get(self.PROTOCOL + self.URL + self.PATH, params=parameters)
          data = json.loads(response.text)
          if "data" in data:
            price = data["data"][self.SYMBOL]["quote"]["USD"]["price"]
            print(price)
            return price            
        except (ConnectionError, Timeout, TooManyRedirects) as e:
          print(e)
        return

if __name__ == "__main__":
    Price().main()
