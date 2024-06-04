#在信息位前加冗余位用于计算总字符数，包括校验位

def charsum(data:str):
    cs = format(len(data),"08b")
    for c in data:
        cs += format(ord(c),"08b")
    return cs

SOH = "00000001"
EOT = "00000100"
ESC = "00011011"


def chardepend(data:str):
    """
    在首位添加控制字来确定界限，如果信息位中有这两个控制字符则在字符前使用转移字符转义
    首 SOH ascll值 00000001
    尾 EOT ascll值 4 00000100
    转义 ESC ascll值 27 00011011
    """ 
    ff = SOH
    for c in data:
        asc = format(ord(c),"08b")
        if asc == SOH or c == EOT:
            ff += ESC
        ff += asc
    ff += EOT
    return ff


zerobound = "01111110"
def zerodepend(data:str):
    """
    用01111110作为首尾帧界，信息位出现5个连续的1时插入一个0
    """
    ff = ""
    for c in data:
        ff += format(ord(c),"08b")
    
    i = ff.find("11111")
    while i != -1:
        ff = ff[:i+5] + "0" + ff[i+6:]
        i = ff.find("11111")
    ff = zerobound + ff + zerobound    
    return ff  
        
if __name__ == "__main__":
   print(zerodepend("aa"))

