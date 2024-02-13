from brownie import accounts, Faucet

def main():
    maccount = accounts[0]
    contract_account = Faucet.deploy({'from':maccount})
    print(contract_account.address)
    print(contract_account.balance())
    print(maccount.address)
    print(maccount.balance())
    maccount.transfer(contract_account.address, 10)
    contract_account.withdraw(10, {'from': maccount})
