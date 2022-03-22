from stellar_sdk import Keypair, Network, Server, TransactionBuilder, Account
import os
from dotenv import load_dotenv
from pathlib import Path
import logging


logging.basicConfig(filename='account.log', encoding='utf-8', level=logging.INFO)
load_dotenv()

def main(acc_name):
	source_key = os.getenv(acc_name)
	print("Account: ", acc_name)
	server = Server(horizon_url="https://horizon-testnet.stellar.org")
	acc = server.accounts().account_id(source_key).call()
	print("Balance: ", acc["balances"])
	logging.info(acc_name + "has" + str(acc["balances"]))

if __name__ == "__main__":
	import sys
	if len(sys.argv) <= 1:
		print("missing account name: PUBLIC(int 1-3)")
		exit()
	account = sys.argv[1]
	main(account)
