import socket
if __name__ == "__main__":
    a=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    a.bind(("127.0.0.1",10))
    a.listen(3)
    while 1:
        _,d = a.accept()
        print(d)
       
    a.close()
