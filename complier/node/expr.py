from node.node import *
from abc import ABC, abstractmethod 
class Expr(Node):
    def __init__(self) -> None:
        super().__init__()
class Id(Expr):
    pass    
               
class Op(Expr):
    ADD='+'
    SUB='-'
    MUL='*'
    DIV='/'
    def __init__(self ,v ,v1,op:str=ADD) -> None:
        
class Assign(Expr):
    pass
class Cond(Expr):
    pass
class Rel(Expr):
    pass
class Access(Expr):
    def __init__(self,id:Id,expr:Expr) -> None:
        self.id = id
        self.expr = expr
        

def lvalue(e:Expr) -> Expr:
    """
    计算左值   计算左值可能是变量或者数组
    Returns:
        Expr: 如果是ID则返回本节点
              如果节点
    """
    if isinstance(e,Id):
        return e
    elif isinstance(e,Access):
        return Access(e.id,rvalue(e.expr))
    else:
        raise Exception
def rvalue(self,e:Expr):
    """_summary_
    
    Returns:
        _type_: _description_
    """
    if isinstance(e,Op):
        t = 
    return 1         