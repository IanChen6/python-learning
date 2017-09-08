import math
def is_prime(n):
    list_num = []
    for i in range(2, n):
        for num in range(2, int(sqrt(n))+1):
            if i % num == 0 and i != num:
                break
            elif i % num != 0 and num == (int(sqrt(n))):
            list_num.append(i)
     return list_num
print(is_prime(100))