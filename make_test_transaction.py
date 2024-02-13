from web3 import Web3

# Connect to Ganache
# ganache_ws_url = "ws://127.0.0.1:7545"  # Ganache default URL
ganache_ws_url = "ws://127.0.0.1:8545"
# ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.WebsocketProvider(ganache_ws_url))
# web3 = Web3(Web3.HTTPProvider(ganache_url))

mnemonic = (
    "myth like bonus scare over problem client lizard pioneer submit female collect"
)
account_path_template = lambda index: f"m/44'/60'/0'/0/{index}"
init_account_count = 20
chainId = 1

import brownie
import eth_account
from web3.middleware import construct_sign_and_send_raw_middleware

eth_account.Account.enable_unaudited_hdwallet_features()

# Check connection status
if web3.is_connected():
    print("Connected to Ganache/Geth")
    # print("accounts before:", web3.eth.accounts) # you still gets all accounts.

    genesis_account = web3.eth.account.from_key(
        "0x423c19a7c53ac3a782b38c1b3d3fb51c0c2eae413c2d6ecd1259fbe7942cbea9"
    )
    web3.middleware_onion.add(construct_sign_and_send_raw_middleware(genesis_account))
    genesis_balance = web3.eth.get_balance(account=genesis_account.address)
    print("Account Genesis:", genesis_balance)
    if genesis_balance != 0:
        from web3.middleware import geth_poa_middleware
        
        # web3.geth.personal.unlock_account(genesis_account.address, "ethereum")

        # inject the poa compatibility middleware to the innermost layer (0th layer)

        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        # transfer.
        web3.eth.send_transaction( # the account amount is not reflected.
            {
                "from": genesis_account.address,
                "to": brownie.ZERO_ADDRESS,
                "value": web3.to_wei(1, "ether"),
                # "chainId":1234,
            }
        )
        print("Account Genesis:", web3.eth.get_balance(account=genesis_account.address))
        print(
            "Account Zero:",
            web3.eth.get_balance(
                account=brownie.ZERO_ADDRESS
            ),  # this address is not good. we cannot get money from it.
        )  # it does get the transaction fee.

    else:

        for index in range(init_account_count):
            account = web3.eth.account.from_mnemonic(
                mnemonic=mnemonic, account_path=account_path_template(index)
            )  # with address and key.
            web3.middleware_onion.add(
                construct_sign_and_send_raw_middleware(account)
            )  # unlock locally.
        # print("accounts after:", web3.eth.accounts)

        web3.eth.send_transaction(
            {
                "from": web3.eth.accounts[0],
                "to": web3.eth.accounts[1],
                "value": 1,  # it must be the right name, not "amount" but "value"
            }
        )
        print("Transaction sent (1 wei)")  # you send transaction anyway.

        print("Account 0:", web3.eth.get_balance(account=web3.eth.accounts[0]))
        print("Account 1:", web3.eth.get_balance(account=web3.eth.accounts[1]))

        print(
            "Account Coinbase:",
            web3.eth.get_balance(
                account=brownie.ZERO_ADDRESS
            ),  # this address is not good. we cannot get money from it.
        )  # it does get the transaction fee.

        custom_method_name = "evm_setAccountBalance"  # you may not want to expose the ganache endpoint. you just want a wrapped up version of account management service.

        # Make the custom RPC call with method name and JSON payload
        response = web3.manager.request_blocking(
            custom_method_name, [brownie.ZERO_ADDRESS, "0x1"]
        )  # answered! and you do not need authorization.

        print("Custom RPC Response:", response)  # True
        print("Account Coinbase:", web3.eth.get_balance(account=brownie.ZERO_ADDRESS))
else:
    print("Connection to Ganache/Geth failed")
