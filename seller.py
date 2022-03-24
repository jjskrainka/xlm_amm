"""
This class simulates a bidder for the amm liquidity pool. It sources a price from CoinMarketCap. It then uses this as a reference price which it applies a set spread to that would result in a favorable transaction for itself.
"""
from stellar_sdk import Account, Asset, Keypair, Network, TransactionBuilder, LiquidityPoolAsset
from helpers import get_sequence, connect_horizon, create_trust
from price import Price
from stellar_sdk.operation.path_payment_strict_receive import PathPaymentStrictReceive
from liquidity_pool import get_lp_id
import os


# LEVELS (SPREAD, AMOUNT) represents an offset from the reference price (SPREAD) followed by an amount of the asset to transact at
# that given spread. The larger the spread, the more favorable the transaction, so the overall AMOUNT would be greater.
LEVELS = [[0.025, 1], [0.005, 2], [0.02, 3]]

seller_secret = os.environ.get("SELLER_SECRET")
seller_keypair = Keypair.from_secret(
            seller_secret
)
sequence = get_sequence(seller_keypair.public_key)

# Create an Account object from an address and sequence number.
seller_account = Account(account=seller_keypair.public_key, sequence=sequence)
reference_price = Price().main()
lp_account_id = os.environ.get("LIQUIDITY_POOL")

destination =  get_lp_id()
send_asset = Asset.native()
send_max = LEVELS[0][1]
dest_asset = LiquidityPoolAsset(Asset.native(), Asset("USD", lp_account_id))  # liquidity pool asset 
dest_amount = reference_price + LEVELS[0][0]

create_trust(seller_account, dest_asset, seller_secret)
transaction = (
    TransactionBuilder(
        source_account=seller_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .add_text_memo("Making market as a seller")
    .append_liquidity_pool_withdraw_op(
        liquidity_pool_id=destination,
        amount=str(round(LEVELS[0][1] / 10000000, 7)),
        min_amount_a=str(round(1 / 1000000, 7)),  # because we are referencing USD price of 1 XLM
        min_amount_b=str(round(dest_amount / 1000000, 7))  # reference price in USD with spread
    )
    .set_timeout(30)
    .build()
)
print(transaction)
transaction.sign(seller_keypair)
response = connect_horizon().submit_transaction(transaction)
print(response["successful"])


