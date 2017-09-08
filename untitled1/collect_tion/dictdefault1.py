# from collections import defaultdict
# dd=defaultdict(lambda :'da')#key不存在时返回“da’
# dd['1']='aba'
# print(dd['1'])
# print(dd['2'])

#为了保持key的顺序
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
d1={"a":1,"b":2,"c":3}
for a in d1:
    print(a)
print(d1)
od = OrderedDict ([('a',1),('b',2),('c',3)])
print(od)
