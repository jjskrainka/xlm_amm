from stellar_sdk import Server, Network, TransactionBuilder 
from stellar_sdk.operation.change_trust import ChangeTrust
import requests

def connect_horizon():
    return Server(horizon_url="https://horizon-testnet.stellar.org") 

def change_trust(asset_object, receiver_address, horizon):
    # Operation Object
    op = ChangeTrust(
        asset=asset_object,
        limit='5000',
        source=receiver_address
    )  
    # Getting the next sequence of the address
    sequence = horizon.account(receiver_address).get('sequence')
    return op, sequence

def fund_account(address):
    r = requests.get('https://horizon-testnet.stellar.org/friendbot?addr=' + address)
    return r.text

def get_sequence(address):
    horizon = connect_horizon()
    sequence = horizon.load_account(address).sequence
    return sequence

def create_trust(seller_account, asset, seller_secret, base_fee=100):
    print(
        "The Seller Account must trust the new asset. \
          \nCreate Trust."
    )
    trust_transaction = (
        TransactionBuilder(
            source_account=seller_account,
            network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
            base_fee=base_fee,
        )
    #  The `changeTrust` operation creates (or alters) a trustline
    #  The `limit` parameter below is optional
    .append_change_trust_op(
        asset=asset,
        )
        .set_timeout(30)
        .build()
    )

    trust_transaction.sign(seller_secret)
    trust_transaction_resp = connect_horizon().submit_transaction(trust_transaction)
    print("Trust created\n")

