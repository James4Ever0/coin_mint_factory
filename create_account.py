from eth_account import Account
from eth_account.signers.local import LocalAccount

# Generate a new private key
account: LocalAccount = Account.create()
account_address = account.address

print("New Private Key:", account.key.hex())
print("Corresponding Account Address:", account_address)

# ganache is not for production. use sqlite instead.