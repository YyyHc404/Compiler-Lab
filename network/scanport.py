import socket
import getopt


def usage():    
    print("Useage: scanport -a target_address")
    print("""-p    - if If specified,scan only one to target port """)
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
    args=sys.argv[1:]   
    shrot="ha:p:"
    address=''
    port=''
    if len(args) == 0:
        usage()
        sys.exit(0)    
    try:
        opts,arg=getopt.getopt(args,shortopts=shrot)
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt,arg in opts:
        if "-a" in opt:
            address=arg
        elif "-p" in opt:
            port = arg
        elif "-h" in opt:
            usage()
            sys.exit(0)
    if address == "":
        print("must spicifed target address")
        sys.exit(2)
    elif port == '':
        scan(address)
    else: 
        scans(address,port)
    
    
