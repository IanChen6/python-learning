from collections import namedtuple
point=namedtuple('p1',['x','y'])
p=point(1,2)
print(p.x)
print(type(p))
print(isinstance(p,tuple))