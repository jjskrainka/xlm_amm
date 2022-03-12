import requests as r
from stellar_sdk import Server



class AutomatedMarketMaker(object):
	http_header = {"Accept": "text/event-stream"}
	https://horizon.stellar.org/order_book?
	protocol = "https"
	domain = "horizon.stellar.org"
	path = "order_book"

	sell_asset_type = "native"
	buy_asset_type = "buying_asset_type=credit_alphanum4"
	asset_code = "BB1"

	

	print(r.get(f'{protocol}://{domain}/{path}?selling_asset_type={sell_asset_type}&sbuying_asset_type={buy_asset_type}&buying_asset_code={asset_code}&buying_asset_type={native,credit_alphanum4,credit_alphanum12}&buying_asset_issuer={:account_id}&buying_asset_code{:asset_code}&limit={1-200}'))

if __name__ == "__main__":
	AutomatedMarketMaker()
