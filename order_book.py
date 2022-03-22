import requests as r
from stellar_sdk import Server, Asset
from stellar_sdk.call_builder.base.base_orderbook_call_builder import BaseOrderbookCallBuilder
import os
from helpers import connect_horizon


class OrderBook(object):
    """
    SDK approach needs more paramaters to return specific order book. Choosing to use https request.
    server = connect_horizon()
    usd = Asset("USD", os.environ.get("PUBLIC2"))
    native = Asset.native()
    ob = server.orderbook(native, usd)
    print(ob)
    """
    protocol = "https://"
    domain = "horizon-testnet.stellar.org/"
    path = "order_book"
    sell_asset_type = "native"
    buy_asset_type = "credit_alphanum4"
    buy_asset_code = "USD"
    buy_asset_issuer = os.environ.get("PUBLIC2")

    ob = r.get(protocol + domain + path + "?" + f"selling_asset_type={sell_asset_type}&buying_asset_type={buy_asset_type}&buying_asset_code={buy_asset_code}&buying_asset_issuer={buy_asset_issuer}")
    print(ob.text)


if __name__ == "__main__":
    OrderBook()
