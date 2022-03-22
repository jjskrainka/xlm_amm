from stellar_sdk import Server 
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
