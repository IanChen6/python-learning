import struct
i2b=struct.pack(">I",123456)#pack的第一个参数是处理指令，
# '>I'的意思是：
#>表示字节顺序是big-endian，也就是网络序，
# I表示4字节无符号整数。
print(i2b)