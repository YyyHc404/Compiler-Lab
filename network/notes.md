#### 环回地址:
     数据将通过回环接口（loopback interface）发送和接收。回环接口是计算机内部的虚拟网络接口，用于在同一台计算机上的进程之间进行通信。
    环回地址只是用于本地进程通讯

#### 套接字：
        保存了进程所需网络的状态和数据结构，为应用程序提供了API进行网络通讯，对套接字操作时触发系统调用，操作系统进行网络通讯


## python: 
#### 套接字类型:
- AF_PACKET 是一个直接连接网络设备的低层级接口。
- AF_HYPERV是一种地址族，用于与Hyper-V虚拟化平台通信。在Python的socket模块中，AF_HYPERV用于创建与Hyper-V之间的通信套接字。Hyper-V是微软的虚拟化平台，允许在Windows操作系统上创建和管理虚拟机。通过AF_HYPERV地址族，可以实现主机与虚拟机之间的通信，以及虚拟机之间的通信。
- AF_NETLINK 与内核通讯的地址簇
#### 其他:
- socket.ioctl 用于执行套接字的 I/O 控制操作
- socket.getaddrinfo    将地址和port等socket信息转换转换为

## API 文档:
https://docs.python.org/zh-cn/3/library