# PyCoin #
A fun educational set of functions for creating and customizing a blockchain built using Python.

# Overview # 
This blockchain was made following the standards of the bitcoin white paper, it uses proof of work as a consesus mechanism, this proof of work is called mining and it is also in mining where the miner writes the pending transactions to a block.

## Blocks ##
Explain the block.

## Transactions ##
Explain the block.

## Network ##
Explain the block.

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
