# PyCoin #
A fun educational set of functions for creating and customizing a blockchain built using Python.

# Overview # 
This blockchain was made following the standards of the bitcoin white paper, it uses proof of work as a consesus mechanism, this proof of work is called mining and it is also in mining where the miner writes the pending transactions to a block.

## Blocks ##
Explain the block.

## Transactions ##
A transaction is a piece of data written inside each block, each transaction is hashed and together these hashes are in turn hased to form a root hash - what is known as a merkle tree:
[<p align="center"><img src="https://miro.medium.com/max/447/1*1e-wyMbvf8-u7Le1LUxTBA.png" width="600px"/></p>](https://miro.medium.com/max/447/1*1e-wyMbvf8-u7Le1LUxTBA.png)\
This root hash will server as the unqiue indeitifer for the block's transaction.

Each transaction is hashed together much like how the blocks previous hash is found inside the current block, this is done to increase the security of the transcation data. For example Alice sends Bob 10 PyCoin's and Bob sends Alice 1 PyCoin 3 times; the chronological list of transactions will be:
Alice - 10 PyC - Bob\
Bob - 1 PyC - Alice\
Bob - 1 PyC - Alice\
Bob - 1 PyC - Alice\


[<p align="center"><img src="https://www.researchgate.net/profile/Sinisa-Randic/publication/324791073/figure/fig1/AS:660241230340097@1534425184691/The-structure-of-transaction-in-a-Bitcoin-blockchain.png" width="800px"/></p>](https://www.researchgate.net/profile/Sinisa-Randic/publication/324791073/figure/fig1/AS:660241230340097@1534425184691/The-structure-of-transaction-in-a-Bitcoin-blockchain.png)\


## Network ##
After the blockchain node has mined a block it will then send it to the network in hopes it will be written to the networks blockchain, here is a good illustration that demonstrates the protocol in which a transaction makes it way into the blockchain.

![A transaction's journey.](https://www.researchgate.net/publication/320518549/figure/fig2/AS:551464202637312@1508490719530/A-bitcoin-transaction.png)\


# Get Started #
Currently, there are three components:
 - ___app___: An API - creates an instance of ___pycoin___.
 - ___pycoin___: The blockchain node. 
 - ___webui___: A web-based UI for the API.

To launch the app:

`cd app`\
`flask --app main --debug run`

And if you want to get into the guts of the node, you can launch it in the terminal:

`cd pycoin`\
`python main.py`

To launch the webui:

`cd webui`\
`node run main.js`
