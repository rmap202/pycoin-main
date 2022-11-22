from pycoin.src.config import SU_ADDR

from src.utils.merkle import hash_contents, root_hash

from src.entities.block import Block
from src.entities.transcation import Transaction

## get an instance of the blockchain db

## do the proof of work on a block and tx

## submit the block to the network and await for pending changes

def mine(blockchain, addr):
       
        # If miner address is valid
        if not (addr):
            return False

        # If its our genesis block
        if (len(blockchain.blocks) == 0):
            prev_hash = "0x00"
        else: 
            prev_hash = hash_contents(blockchain.blocks[-1])

        # If our blockchain has any pending transactions
        if (len(blockchain.pending_txs) > 0):
            txs = blockchain.pending_txs
        else:
            txs = []

        coinbase = Transaction(SU_ADDR, addr, blockchain.get_reward(), [])
        txs.append(coinbase)

        tx_root = root_hash(txs)

        block = Block(txs, blockchain.get_index() + 1, prev_hash, addr, tx_root)

        # Our proof of work
        difficulty = blockchain.get_difficulty()
        while not (hash_contents(block).startswith('0' * difficulty)):
            block.seed += 1

        blockchain.blocks.append(block)
        blockchain.curr_supply = blockchain.get_current_supply()
        blockchain.pending_txs = []

        return True


    # def validate_tx(self, tx):
    #     wallet = Wallet(tx.from_addr)
    #     bal = wallet.get_wallet_bal(self.blocks, self.pending_txs)
    #     print(bal)
    #     if (int(tx.amount) > bal):
    #         return False

    #     self.pending_txs.append(tx)
    #     return True

    # def verify_blocks():
    #     pass
        # verify each block prev_tx matches
        # and seed matches



    # def mine_block(self, miner_address):

    #     difficulty = self.get_difficulty()
    #     amount = 10**(1/difficulty)

    #     if not (miner_address):
    #         return False

    #     if (len(self.blocks) == 0):
    #         prev_hash = "0x00"
    #     else: 
    #         prev_hash = hash_contents(self.blocks[-1])

    #     if (len(self.pending_txs) > 0):
    #         txs = self.pending_txs
    #     else:
    #         txs = []

    #     coinbase = Transaction("0x00", miner_address, int(amount), ["coinbase"], self.blocks, self.pending_txs)

    #     txs.append(coinbase)
    #     tx_root = root_hash(txs)

    #     block = Block(txs, len(self.blocks), prev_hash, miner_address, tx_root)

    #     while not (hash_contents(block).startswith('0' * difficulty)):
    #         block.seed += 1

    #     self.blocks.append(block)
    #     self.curr_supply = self.get_current_supply()
    #     self.pending_txs = [] # remove txs

    #     return True
