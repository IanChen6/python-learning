# def isodd(n):
#     return n%2==0
# r=filter(isodd,[1,2,3,4,5,6,7,8,9,10])
# print(list(r))#案例1选出偶数

# def empty(s):
#     return s.strip()
# l=['  sdsd','sds dafa ','sd fwq',"","\r"]
# r=filter(empty,l)
# print(list(r))
#删除序列中的空白字符串

# s='  123    '
# a=s.strip()
# print(s and s.strip())

#用filter求素数
# def odd_iter():#生成从3开始的奇数序列
#     n=1
#     while True:
#         n=n+2
#         yield n
# def is_not_divisible(n):#筛选出不可除尽的奇数
#     return lambda x:x%n>0
# def primes():
#     yield 2
#     it = odd_iter()# 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(is_not_divisible(n), it) # 构造新序列
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

#用filter筛选回数
def is_palindrome(n):
    s=str(n)
    for i in range(len(s)):
        if s[i]==s[len(s)-1-i]:
            return True
        else:
            return False
out=filter(is_palindrome,range(1000))
print(list(out))
