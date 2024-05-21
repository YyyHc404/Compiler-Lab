import socket
import struct

class udp:
    def __init__(self, src_port: int, des_port: int, data: str, src_ip: str, des_ip: str) -> None:
        self.src_port = src_port
        self.des_port = des_port
        self.src_ip = src_ip
        self.des_ip = des_ip
        self.data = data.encode()  # 直接对字符串进行编码
        self.udp_length = len(self.data) + 8  # UDP长度包括头部和数据

        # 构建UDP伪头部（pseudo-header）和UDP头部
        self.pseudo_header = struct.pack('!4s4sBBH', socket.inet_aton(self.src_ip), socket.inet_aton(self.des_ip), 0, socket.IPPROTO_UDP, self.udp_length)
        self.udp_header = struct.pack('!HHHH', self.src_port, self.des_port, self.udp_length, 0)  # 初始校验和字段为0

        # 组合UDP报文段
        self.udp_packet = self.pseudo_header + self.udp_header + self.data

        # 计算校验和
        self.caclcksm = self.calccksm()

        # 将校验和填充到UDP头部
        self.udp_header = struct.pack('!HHHH', self.src_port, self.des_port, self.udp_length, socket.htons(self.caclcksm))
        self.udp_packet = self.pseudo_header + self.udp_header + self.data

    def calccksm(self) -> int:
        """
        计算UDP校验和
        """
        # 16位对齐，如果不是16位对齐，在数据后补0
        if len(self.udp_packet) % 2 != 0:
            self.udp_packet += b'\0'

        # 初始化校验和为0
        checksum = 0

        # 对每个16位进行求和
        for i in range(0, len(self.udp_packet), 2):
            word = self.udp_packet[i:i+2]
            checksum += struct.unpack('!H', word)[0]

        # 处理进位，直到没有进位为止
        while (checksum >> 16) > 0:
            checksum = (checksum & 0xFFFF) + (checksum >> 16)

        # 取反得到最终的校验和
        checksum = ~checksum & 0xFFFF

        return checksum

    def strform(self) -> bytes:
        """
        返回UDP报文段的字节串形式
        """
        return self.udp_packet

# 客户端发送函数等其他代码...

if __name__ == "__main__":
    # 测试代码
    udp_packet = udp(123, 123, "Hello UDP", "192.168.1.1", "192.168.1.2")
    print(udp_packet.strform().hex())