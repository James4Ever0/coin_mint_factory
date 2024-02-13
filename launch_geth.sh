# you cannot create eth coin here. but you can set the coinbase address to your address.
geth --datadir ./geth_database --nodiscover --ws --ws.api "eth,net,web3,personal" --ws.addr "localhost" --ws.port 8545 --networkid 12345 --mine --miner.etherbase=1347a796EC600aeDf4bF5aC448faA6C3FBC9a46c --unlock=1347a796EC600aeDf4bF5aC448faA6C3FBC9a46c --password=password --allow-insecure-unlock  --miner.gasprice=0

# geth --datadir ./geth_database --nodiscover --ws --ws.api "eth,net,web3,personal" --ws.addr "localhost" --ws.port 8545 --mine --miner.threads=1 --miner.etherbase=0x0000000000000000000000000000000000000001

# address other than the zero address.