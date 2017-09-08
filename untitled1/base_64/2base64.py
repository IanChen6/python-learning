import base64
# b2=base64.b64encode(b'binary\x00string')
# print(b2)
# b1=base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
# print(b1)


#处理去掉=号的base64函数
def safe_base64_decode(s):
    # mod = int(len(s)) % 4
    # if mod != 0:
    #    for i in range(4-mod):
    #        s=s+b"="
    # return base64.urlsafe_b64decode(s)
    # s1 = str(s,encoding='utf8')
    while len(s)%4 != 0:

        s += "="
    # s1=bytes(s1,encoding='utf8')
    return base64.b64decode(s)
print(safe_base64_decode('urasshol'))