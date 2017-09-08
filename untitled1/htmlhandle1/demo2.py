from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib
from urllib import request
url="https://www.python.org/events/python-events/"
global content
content=urllib.request.urlopen(url).read()
content=content.decode("utf8")
# print(content)
eventDic={}
titleFlag=0
timeFlag=0
locationFlag=0
printFlag=0
title=''
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global eventDic,titleFlag,timeFlag,locationFlag,title
        for (variable,value) in attrs:
            if r'/events/python-events/' in value:
                titleFlag = 1
            if variable=='datetime':
                eventDic[title]['time']=value[:10]
            if value=='event-location':
                locationFlag=1

    def handle_endtag(self, tag):
        global eventDic,title,printFlag
        if printFlag:
            print('%s:%s'%(title,eventDic[title]))
            printFlag=0

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        global eventDic,titleFlag,title,locationFlag,printFlag
        if titleFlag:
            eventDic[data]={'title':data}
            titleFlag=0
            title=data
        if locationFlag:
            eventDic[title]['location']=data
            locationFlag=0
            printFlag=1

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass
parser=MyHTMLParser()
parser.feed(content)