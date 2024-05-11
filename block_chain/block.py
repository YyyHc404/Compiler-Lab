import time


class Block:
    def __init__(self,timestamp:int,nonce:int,data:str,preblockhash:str,hash:str) -> None:
        self.timestamp = timestamp
        self.data = data
        self.preblockhash = preblockhash
        self.hash = hash
        self.nonce = nonce

def newBlock(data:str,preblockhash:str)-> Block:
    global targetBits
    """
    创建计算后的新块
    """
    ts = int(time.time())
    block = Block(preblockhash=preblockhash,
                  data=data,
                  timestamp=ts,
                  hash='',
                  nonce=0)
    from proofofwork import ProofOfWork
    from proofofwork import Run
    pow = ProofOfWork(block=block)
    nonce,hash= Run(pow)
    block.hash = hash
    block.nonce = nonce 
    return block    
def newGenesisBlock() -> Block:
    """
    创建创世区块
    """
    return newBlock("Genesis Block",'')