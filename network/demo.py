# -*- coding: utf-8 -*-

# 包含RLO控制字符的文件名
file_name = "malicious\u202e.exe"

# 将文件名保存到磁盘
with open(file_name, 'w') as file:
    file.write("This is a malicious file.")