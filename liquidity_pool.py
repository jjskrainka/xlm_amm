"""
Interact with liquidity pool. Currently the only method, get_lp_id, returns the liquidity pool ID
"""
from stellar_sdk import (
    Asset,
    Keypair,
    LiquidityPoolAsset,
    Network,
    Server,
    TransactionBuilder,
)
import os

def get_lp_id():
    horizon_url = "https://horizon-testnet.stellar.org/"
    network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE

    server = Server(horizon_url=horizon_url)
    source_keypair = Keypair.from_secret(
    	os.environ.get("SECRET2")
    )

    asset_a = Asset.native()
    asset_b = Asset("USD", os.environ.get("PUBLIC2"))
    liquidity_pool_asset = LiquidityPoolAsset(asset_a=asset_a, asset_b=asset_b)
    liquidity_pool_id = liquidity_pool_asset.liquidity_pool_id
    print(f"Liquidity Pool ID: {liquidity_pool_id}")
    result = server.liquidity_pools().liquidity_pool(liquidity_pool_id)
    print(result.for_account(os.environ.get("PUBLIC2")).call())
    
    return liquidity_pool_id
