**架构**：
- 核心 汇聚 接入

**设备接口**：
- GE(GigabitEthernet)接口 千兆以太网接口
- FE(Fast Ehternet)接口 快速以太网接口，需要更高的传输速度但比千兆网口低
- console接口 用于在本地初始化配置
- auxiliary接口 使用调制解调进行远程登录，用于异步串行连接
- usb接口 可以连接移动网络、文件共享、固件升级
- RJ45 RJ代表已注册的插孔，45代表接口标准的序号
- DHCP：
    - 为某个VLAN分配地址池
    - 排除分配的地址
    - DNS地址
    - 网关地址
    - 网络地址绑定
    - 静态绑定 mac -> ip
        - 命令：
            - 创建地址池：ip pool vlan10 
            - 地址池网络域: network ip mask 0.0.0.3
            - 分配默认DNS: dns-list 
            - 分配默认网关：getway-list 
            - 排除分配地址: excluded-ip-address 
**交换机**：
- AR201
    - 只有WAN可以直接配置IP，是interface Ethernet0/0/8，其它口要通过vlanif来配置IP
 - undo portswitch命令用来配置将以太网接口从二层模式切换到三层模式。            

**VLAN**：
- VLAN接口是一种三层模式下的虚拟接口，主要用于实现VLAN间的三层互通，它不作为物理实体存在于设备上。每个VLAN对应一个VLAN接口，在为VLAN接口配置了IP地址后，该接口即可作为本VLAN内网络设备的网关，对需要跨网段的报文进行基于IP地址的三层转发。
- 根据端口在转发报文时对Tag标签的不同处理方式，分为三种：
    - TRUNK：允许多个VLAN标签通过
    - Access：端口只能属于1个VLAN
    - Hybrid: 允许多个VLAN通过接收和发送多个VLAN的报文,Hybrid端口既可以连接接入链路又可以连接干道链路
- 命令：
    - 批量创建：vlan batch
    - 进入VLAN端口：int vlanif 
    - 进入端口后：
        - 配置该端口VLAN端口类型： port link-type
        - 配置端口所属VLAN 
    - 每个VLAN对应一个VLANIF接口，而这个接口可以被配置一个IP地址，从而充当该VLAN内主机的默认网关。
- VLAN原理：
    - 以标准化VLAN实现方案的IEEE 802.1Q
    - 原数据帧格式:DA&SA Type Data
    - 目的MAC地址和源MAC地址之后封装4个字节的VLAN Tag，用以标识VLAN的相关信息。
    - VLAN帧: 在DA&SA后
        - TPID用来判断本数据帧是否带有VLAN Tag，长度为16bit，缺省取值为0x8100。
        - Priority表示报文的802.1P优先级，长度为3bit，相关内容请参见“ACL和QoS配置指导”中的“QoS”。
        - CFI字段标识MAC地址在不同的传输介质中是否以标准格式进行封装，长度为1bit，取值为0表示MAC地址以标准格式进行封装，为1表示以非标准格式封装，缺省取值为0。
        - VLAN ID标识该报文所属VLAN的编号，长度为12bit，取值范围为0～4095。由于0和4095为协议保留取值，所以VLAN ID的取值范围为1～4094。
- VLAN 划分:
    - 基于端口
    - 基于MAC地址
    - 基于协议
    - 基于IP子网
    - 基于策略
- 不同VLAN间的主机不能直接通信，需要通过路由器或三层交换机等网络层设备进行转发
- 设备提供VLAN接口实现对报文进行三层转发的功能。
- 除了可以设置端口允许通过的VLAN，还可以设置端口的缺省VLAN。在缺省情况下，所有端口的缺省VLAN均为VLAN1，但用户可以根据需要进行配置。
- Access端口的缺省VLAN就是它所在的VLAN，不能配置。
- Trunk端口和Hybrid端口可以允许多个VLAN通过，能够配置缺省VLAN。
- 当执行undo vlan命令删除的VLAN是某个端口的缺省VLAN时，对Access端口，端口的缺省VLAN会恢复到VLAN1；对Trunk或Hybrid端口，端口的缺省VLAN配置不会改变，即它们可以使用已经不存在的VLAN作为缺省VLAN。

- pvid 缺省标签，收到无tag的数据帧时打上默认的pvid，判断是否在放通tag列表里，使用trunk
VLAN间路由:
