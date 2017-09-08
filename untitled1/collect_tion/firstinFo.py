from collections import OrderedDict

class LastUpdateOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdateOrderedDict,self).__init__()
        self.__capacity=capacity

    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0#判断是否已经存在要添加的key
        print('self1=', self)
        if len(self) - containsKey == self.__capacity:#判断是否要删除元素
            print('self2=', self)
            #删除最后的元素
            last = self.popitem(last=False)
            print('remove:', last)
            print('self3=', self)
        if containsKey:
            print('self4=', self)
            del self[key]
            print('set:', (key, value))
            print('self5=', self)
        else:
            print('add:', (key, value))
            print('self6=', self)
        OrderedDict.__setitem__(self, key, value)
        print('self7=', self)
m_od = LastUpdateOrderedDict(2)
m_od['a']=1

