from node.node import *
from abc import ABC, abstractmethod 
class Expr(Node):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def rvalue(self):
        """
        
        """
        pass                     

class Assign(Expr):
    pass
class Cond(Expr):
    pass
class Rel(Expr):
    pass
class Access(Expr)