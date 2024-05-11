

from block_chain import Block_Chain,ProofOfWork
from proofofwork import *


def newBlockChain():
    bc = Block_Chain()
    bc.addBlock("Send 1 BTC to Ivan")
    bc.addBlock("Send 2 BTC to Ivan")
    for block in bc.block_chain:
        pow = ProofOfWork(block)
        print(f"Prev Hash: {block.preblockhash}")
        print(f"Data: {block.data}")
        print(f"Block Hash: {block.hash}")
        print(f"PoW: {Validate(pow)}")
        print()
if __name__ == "__main__":
    newBlockChain() 