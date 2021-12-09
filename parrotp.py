# --------------253 Proj----------------
from web3 import Web3
import time 
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x06Ad6b009b7937B28CfD82A228F7c7E245b55D00'
James_account = '0x1c794E54a6a90A56DaeB63Dfc58c2c8147451Eb2'
Ryan_account  = '0x3CEbe12C391BA03f8dcAAaFF1481fC0516DE70db'


nonce1 = web3_ganache_connection.eth.getTransactionCount(Alice_account)

transaction_data1 = {
    'nonce':nonce1,
    'to':James_account,
    'value':web3_ganache_connection.toWei(50, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(50,'gwei')
}

private_key1 = '7902f4eb5d2f534db18512718e8c42b57d618a0106b932cdc25696c4f3e4fc0c'

singed_transaction1 = web3_ganache_connection.eth.account.signTransaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.sendRawTransaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.toHex(transaction_hash1))



# -----------------
print("WAIT THE HACKERS ARE FINDING THE Etiam hendrerit pretium massa") 
time.sleep(5)
# -----------------



nonce2 = web3_ganache_connection.eth.getTransactionCount(James_account)

transaction_data2 = {
    'nonce':nonce2,
    'to':Ryan_account,
    'value':web3_ganache_connection.toWei(100, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(40,'gwei')
}

private_key2 = 'c8b6e7be97a5a197d2203c1e26f43e9bd8e0dbbfce1a1d89e52f7ac923f8c081'

singed_transaction2 = web3_ganache_connection.eth.account.signTransaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.sendRawTransaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.toHex(transaction_hash2))
