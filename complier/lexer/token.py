class Token:
    """
    一个词法单元类型
    格式:
        <token-name,attribute-value>     
    """
    def __init__(self,token:int) -> None:
        self.tag
        
class Tag:
    """
    Token类型
    """
    ID=256
    NUM=257
    TRUE=258
    FALSE=259

class Num(Token):
    """
    Args:
        value (int) : attribute-value
    """
    def __init__(self,value:int) -> None:
        super().__init__(Tag.NUM)
        self.value=value

class Word(Token):
    """
    Args:
        word (str) : attribute-value
    """
    def __init__(self,word: str) -> None:
        super().__init__(Tag.ID)
        self.word=word
