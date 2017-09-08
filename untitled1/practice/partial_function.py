#!/usr/bin/env python3  #让该文件能在Linux/mac/unix上运行
# -*- coding: utf-8 -*- #注释说明文件使用UTF-8编码
import functools
int2 = functools.partial(int, base=2)
print(int2('100001111'))
#固定命名关键字参数,将base=2作为**kw参数传入

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))#会将10作为*args传入