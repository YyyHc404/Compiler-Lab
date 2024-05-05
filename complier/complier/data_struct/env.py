
class Env:
    """
    每一个作用域的符号表
    块中的变量指向本层和外层最近的声明
    """
    
    def __init__(self,pre : 'Env' = None) -> None:
            self.pre=pre
            self.Symbols = {}
    def put(self,key:str,Symbol) -> None:
        self.Symbols[key] = Symbol
    def get(self,key:str) -> 'Env':
        if self.Symbols[key] is None:
            if self.pre is None: 
                return None 
        return self.pre.get(key)
        
    
    
class Symbol:
    def __init__(self) -> None:
         pass