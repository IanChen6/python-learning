# -*- coding:utf-8 -*-
__author__ = 'IanChen'

import re

string = 'This is a\nnormal string'
a=re.match(r'This',string)
print(a.group())
a.start()
a.end()
print(a.start())
print(a.end())

contactInfo = 'Doe,John:555-1212'
match=re.search(r'(?P<first>\w+),(?P<second>\w+):(?P<third>.*)',contactInfo)
print(match.group('first'))
print(match.group('second'))
print(match.group('third'))

