"""
    基本运算表达式
    9 + 10 - 
    exp -> exp - term   {print('-')}
        |  exp + term   {print('+')}
        |  term 
    term ->  num   
    后缀表达式
    A -> yR
    R -> '-' term  {print('-')} R
        | + term   {print('+')} R
        | E
    term -> num   {print(num)}
"""

class Parser:
    def __init__(self) -> None:
        self.lookhead  = input()
    def exp(self):
        self.term()
        self.rest()       
    def rest(self):
        if self.lookhead == '-' :
            self.match('-')
            self.term()
            print('-')
            self.rest()
        elif self.lookhead == '+' :
            self.match('+')
            self.term()
            print('+')
            self.rest()
        else:
            return
    def term(self):
        if self.lookhead.isdigit():
            print(self.lookhead)
            self.match(self.lookhead)    
        else:
            raise SyntaxError()
    def match(self, c:str) -> bool:    
        if str is self.lookhead:
            raise SyntaxError()
        self.lookhead = input()

if __name__ == "__main__":
    p=Parser()
    p.exp()
    print("\n")