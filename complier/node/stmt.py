from node.node import Node
from node.expr import Expr
from abc import ABC, abstractmethod 
class Stmt(Node):
    
    @abstractmethod
    def gen(self):
        pass

class While(Stmt):
    def __init__(self,) -> None:
        super().__init__()
    pass

class If(Stmt):
    def __init__(self,expr:Expr,stmt: Stmt) -> None:
        self.expr = expr
        self.stmt = stmt
    def gen(self):
        pass
              
class Eval(Stmt):
    pass

class Do(Stmt):
    pass

