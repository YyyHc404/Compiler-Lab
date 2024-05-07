import serial
import serial.tools.list_ports

# 获取可用串口列表
available_ports = serial.tools.list_ports.comports()

# 打印可用串口列表
print("Available Ports:")
for port in available_ports:
    print(port)

# 创建虚拟串口
virtual_port_name = "COM10"  # 指定虚拟串口名称
virtual_port = serial.serial_for_url("loop://" + virtual_port_name, baudrate=9600)

# 打开虚拟串口
virtual_port.open()

# 发送数据到虚拟串口
data_to_send = b"Hello, virtual port!\r\n"
virtual_port.write(data_to_send)
print(f"Sent data to virtual port: {data_to_send}")

# 从虚拟串口接收数据
received_data = virtual_port.readline()
print(f"Received data from virtual port: {received_data}")

# 关闭虚拟串口
virtual_port.close()
