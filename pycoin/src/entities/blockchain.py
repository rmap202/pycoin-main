# from pycoin.block import Block
# from pycoin.transcation import Transaction
# from pycoin.crypto import hash_contents
# from pycoin.merkle import root_hash, hash_map
# from pycoin.wallet import Wallet


# The blockchain entity. It stores fundamental values and contains basic read and write functionalities
class Blockchain:
    def __init__(self):
        self.pending_txs = []
        self.blocks = []
        self.max_supply = 1e+5
        self.curr_supply = 1e+5

    def get_difficulty(self):
        return 1
    
    def get_index(self):
        return len(self.blocks)
    
    # Gets the current supply by adding the amount of money that has been taken from
    # the genesis address.
    def get_current_supply(self):
        current_supply = 0
        for block in self.blocks:
            for tx in block.txs:
                if tx.from_addr == "0x00":
                    current_supply += float(tx.amount)
        return self.max_supply - current_supply
