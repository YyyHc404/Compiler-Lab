import hashlib
from block import Block
targetBits  = 5
class ProofOfWork:
    global targetBits
    def __init__(self,block:'Block') -> None:
        self.target = '0' *targetBits  + str(1 << 256 - targetBits )
        self.block = block
    def preparData(self,nonce:int) -> str:
        global targetBits
        """

        """ 
        data = ''
        data += self.block.preblockhash
        data += self.block.data
        data += hex(self.block.timestamp)
        data += hex(targetBits)
        data += hex(nonce)
        return data
def Run(pow:ProofOfWork):
    """
    给定需要pow的块，挖矿
    """
    nonce = 0
    while True:
        ppd = pow.preparData(nonce)
        pdd_hash = hashlib.sha256(ppd.encode()).hexdigest()
        #print(f"hash: {pdd_hash}")
        if str(pow.target) > pdd_hash:
            break
        else:
            nonce += 1
            continue
        #print("\n\n")
    return (nonce,pdd_hash)

def Validate(pow:ProofOfWork) -> bool:
    """
    pow证明
    """    
    data = pow.preparData(pow.block.nonce)
    return hashlib.sha256(data.encode()).hexdigest() < pow.target