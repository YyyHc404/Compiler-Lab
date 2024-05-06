import socket


def scans(address:str,port:str) -> None:
    """
        只扫描指定端口，如果命令行参数提供了
    """
    
    skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    try:
        skt.connect((address,int(port,10)))
            
    except ConnectionRefusedError:
        print(f"{port} is not open\n")
    else :print(f"{port} is open\n")
    skt.close()

def scan(address:str) -> None:
    """
    暴力扫描该ip上的所有端口
    """
    skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    for  pt in range(1,65535):
        try:
            skt.connect((address,pt))
            
        except ConnectionRefusedError:
            print(f"{pt} is not open\n")
            continue
        except OSError:   
            print(f"{pt-1} open\n")    
            skt.close()
            skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
            
            continue
    skt.close()
if __name__ == "__main__":
    import sys
    l = len(sys.argv)-1    
    
    if l == 0:
        print("Useage: scanport <address> [port]")
    elif l == 1 :
        scan(sys.argv[1])
    else:
        scans(sys.argv[1],sys.argv[2])
    
    
    
