import time
from pycoin.wallet import Wallet
from pycoin.src.utils import hash_contents

class Transaction:

    def __init__(
            self,
            from_addr, 
            to_addr, 
            amount, 
            data, 
            blockchain
        ):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = int(amount)
        self.data = data
        self.timestamp = time.time()

        self.prev_tx = self.get_prev_tx(blockchain.blocks, blockchain.blocks)
        self.hash = self.get_hash()

    def get_prev_tx(self, blocks, pending_txs):
        wallet = Wallet(self.from_addr)
        wallet.get_txs(blocks, pending_txs)
        print(wallet.txs)
        return ""

    def get_hash(self):
        return hash_contents(self)

    def sign(self, priv_key):
        return True 
