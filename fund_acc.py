"""
This example shows how to create and fund a new account with the specified starting balance.

See: https://developers.stellar.org/docs/tutorials/create-account/#create-account
See: https://developers.stellar.org/docs/start/list-of-operations/#create-account
"""
from stellar_sdk import Keypair, Network, Server, TransactionBuilder, Asset

from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(filename='transaction.log', encoding='utf-8')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


source_acc = "SECRET1"
dest_acc = "SECRET2"
logger.debug("Source account: " + f"{os.getenv(source_acc)}")
print("Source account: " + f"{os.getenv(source_acc)}")
server = Server(horizon_url="https://horizon-testnet.stellar.org")
source = Keypair.from_secret(os.getenv(source_acc))
destination = Keypair.from_secret(os.getenv(dest_acc))

print("public key for source", source.public_key)
source_account = server.load_account(account_id=source.public_key)
transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase="'Test SDF Network ; September 2015'",
        base_fee=100,
    )
    .append_payment_op(
        destination.public_key, Asset.native(), "1"
    )
    .set_timeout(30)
    .build()
)
print(os.getenv(source_acc))
transaction.sign(source)
response = server.submit_transaction(transaction)
print(f"Transaction hash: {response['hash']}")
print(
    f"New Keypair: \n\taccount id: {destination.public_key}\n\tsecret seed: {destination.secret}"
)
