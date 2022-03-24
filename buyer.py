"""
This class simulates a bidder for the amm liquidity pool. It sources a price from CoinMarketCap. It then uses this as a reference price which it applies a set spread to that would result in a favorable transaction for itself.
"""
from stellar_sdk import Account, Asset, Keypair, Network, TransactionBuilder, LiquidityPoolAsset
from helpers import get_sequence, connect_horizon, create_trust
from price import Price
from stellar_sdk.operation.path_payment_strict_send import PathPaymentStrictSend
from liquidity_pool import get_lp_id
import os


# LEVELS (SPREAD, AMOUNT) represents an offset from the reference price (SPREAD) followed by an amount of the asset to transact at
# that given spread. The larger the spread, the more favorable the transaction, so the overall AMOUNT would be greater.
LEVELS = [[0.025, 1], [0.005, 2], [0.02, 3]]

buyer_secret =  os.environ.get("SELLER_SECRET") 
buyer_keypair = Keypair.from_secret(
        buyer_secret
)
sequence = get_sequence(buyer_keypair.public_key)

# Create an Account object from an address and sequence number.
buyer_account = Account(account=buyer_keypair.public_key, sequence=sequence)
reference_price = Price().main()
lp_account_id = os.environ.get("LIQUIDITY_POOL")

destination =  get_lp_id()
send_asset = Asset.native()
send_amount = LEVELS[0][1]
dest_asset = LiquidityPoolAsset(Asset.native(), Asset("USD", lp_account_id))  # liquidity pool asset 
dest_min = round(reference_price - LEVELS[0][0], 7)
path = [send_asset, dest_asset]

create_trust(buyer_account, dest_asset, buyer_secret)
transaction = (
    TransactionBuilder(
        source_account=buyer_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .add_text_memo("Making the market as a buyer")
    .append_liquidity_pool_deposit_op(
        liquidity_pool_id=destination,
        max_amount_a=str(11 / 1000000),
        max_amount_b=str(1 / 1000000),
        min_price=str(1 / (reference_price + 1) / 1000000),
        max_price=str(1 / reference_price)
    )
    .set_timeout(30)
    .build()
)
print(transaction)
transaction.sign(buyer_keypair)
response = connect_horizon().submit_transaction(transaction)
print(response["successful"])


