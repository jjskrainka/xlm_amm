"""
Class to query most popular USDC/XLM liquidity pool order book to try to provide a better exchange rate and boost my own LP usage
"""
import requests as r
from stellar_sdk import Server, Asset
from stellar_sdk.call_builder.base.base_orderbook_call_builder import BaseOrderbookCallBuilder
import os
from helpers import connect_horizon


class OrderBook(object):
    server = connect_horizon()
    server = Server(horizon_url="https://horizon.stellar.org")
    usd = Asset("USDC", "GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN")  # use most popular USDC pool to try and beat
    native = Asset.native()
    ob = server.orderbook(native, usd)
    ob = ob.call()
    asks = ob["asks"]
    bids = ob["bids"]
    print("-"*25, "\nBIDS: ", bids)
    print("-"*25, "\nASKS: ", asks)

    def get_bids(self):
        return bids

    def get_asks(self):
        return asks

if __name__ == "__main__":
    OrderBook()
