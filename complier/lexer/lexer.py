from .token import *
from complier.util import Util    
class lexer:
    """
    词法分析器
    """
    
    def __init__(self) -> None:
        """
        保留BOOLEN Token
        """
        self.line=1
        self.words = {}
        self.words["TURE"] = Word("TURE")
        self.words["FALSE"] = Word("FALSE")
        
   
    def scan(self) -> Token: 
        """
        扫描文本，剔除空白符或制表符，记录行数，用于调试。提取一个完整的标识符和数字
        """
        stringBuffer = [] 
        peek=''
        isAnnotaion=False
        for peek in input():
            #剔除空白符
            if peek is '' or peek is '\t' or isAnnotaion: continue
            if peek is '#' or peek: 
                isAnnotaion = True
                continue 
            
            elif peek is '\n': 
                self.line+= 1
                isAnnotaion=False
            
            #整形处理
            if peek.isdigit():
                stringBuffer.append(peek)
                for c in input:
                    if c.isdigit():
                        stringBuffer.append(peek)
                    else: 
                        break
                nt = Num(Util.StringToInterger(stringBuffer))
                return nt
        
                
        stringBuffer.clear()                   
            
       
    def repreve(self,key:str,token:Token) -> Token:
        """
        将token存储在字符表中
        Args:
            key (str):     hash value to retrieval
            token (Token): save Token for you need 

        Returns:
            Token: return Token in words if Token has existed 
        """
        if self.words[str] == None:
            self.words[str]=Token
        else:
            return self.words[str]
        