from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print("a start tag:",tag,self.getpos())#HTMLParser.getpos():返回当前的行号和偏移位置
parser=MyHTMLParser()
print(parser.feed('<div><p>"hello"</p></div>'))