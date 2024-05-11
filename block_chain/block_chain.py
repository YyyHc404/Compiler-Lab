
import typing

from proofofwork import *
from block import * 
class Block_Chain:
    
    block_chain:typing.List['Block'] = []
    def __init__(self) -> None:
        """
        创建区块链，并生成创世区块
        """
        self.block_chain.append(newGenesisBlock())    

    def addBlock(self,data:str) -> None:
        """
        添加新区块到链
        """
        bc = self.block_chain
        pbh = self.block_chain[len(bc) -1].hash
        nb = newBlock(data=data,
                      preblockhash=pbh)
        self.block_chain.append(nb)
        
     
