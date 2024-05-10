listen=False
command=False
port=''
excute=''
upload=''
target=''
upload_destination=''
"""
    netcat tools:
        send data to remote server in standard input
        listen port
        execute command
        revice file
    
"""
def usage():
    print("Netcat Tool")
    print("Usage: netcat -t [target_host] -p [prot]")
    print("-h  --help                       -this cruft")
    print("-l  --listen                     -listen on [host]:[port] for imcoming connections")
    print("-e  --excute file                -excute the given file upon receiving connections")
    print("-c  --command                    -excute the receiving command")
    print("-u  --upload file                -upon receiving connections upload a file and write to [destination]")
    print()
    print()
import sys
import getopt  
import socket
def main():
    global listen
    global port
    global target 
    
    short_opt = ["ht:p:le:cu"]
    long_opt=["--help","--listen","--excute","--command","--upload"]
    opts,args= getopt.getopt(sys.argv,)
    for opt,arg in opts:
        if opt in ("-h","--help"):
            pass
        if opt in ("-h","--help"):
            pass
        
    if not listen and port> 0 and len(target):
        pass
    else:
        pass

def client_sender(buffer:str) -> None:
    """
        向远程服务器发送数据获取响应并输出在发送
    """
    global port
    global target
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        client.connect((target,port))
        if len(buffer):
            client.send(buffer)
        while True:
            response = ''
            while True:    
                data = client.recv(4096)
                response += data
                if len(buffer) < 4096:
                    break
            print(response)
            buffer = input()
            buffer += '\n'
            client.send(buffer)
    except:
        print("[*]EXCEPTION EXIT")
        client.close()

import threading  
import subprocess
def server_loop() -> None:
    """
    开启多线程执行,绑定本地接口，默认 监听全部接口0.0.0.0
    """
    global target
    if target == None:
        target = "0.0.0.0"     
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(target,port)
    server.listen(5)
    while True:
        client,addr= server.accept()
        client_thread = threading.Thread(target=client_handle,args=(client,))
        client_thread.start()



def run_command(command:str) -> str:
    command = command.rstrip()
    try:
        output = subprocess.check_output(command,subprocess.STDOUT,shell=True)
    except:
        print("Faild to excute command.\r\n")
    return output


def client_handle(client:socket.socket):
    global excute
    global upload
    global command
    if len(upload):
        buffer = ''
        while True:
            data = client.recv(4096)
            if not data:
                break
            else:
                buffer += data
        try:
            file = open(upload_destination,"w")
            file.write(buffer)
            file.close()
            client.send("Success receive")
        except:    
            client.send("Faild receive")
    else command:
         