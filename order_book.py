import requests as r
from stellar_sdk import Server, Asset
from stellar_sdk.call_builder.base.base_orderbook_call_builder import BaseOrderbookCallBuilder
import os
from helpers import connect_horizon


class OrderBook(object):
    server = connect_horizon()
    usd = Asset("USD", os.environ.get("LIQUIDITY_POOL"))
    native = Asset.native()
    ob = server.orderbook(native, usd)
    print(ob.call())


if __name__ == "__main__":
    OrderBook()
