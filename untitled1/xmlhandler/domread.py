#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')
#xml.dom.minidom.parse() 用于打开一个xml文件，并将这个文件对象dom变量
#得到文档元素对象
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print (root.nodeType)
print (root.ELEMENT_NODE)