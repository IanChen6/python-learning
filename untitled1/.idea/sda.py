#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
import sys
print(len("中文"))
print(sys.getdefaultencoding())
print(len("中文".encode("utf-8")))
print(sys.getdefaultencoding())
import scrapy
