#未装BS4
from urllib import request
from bs4 import BeautifulSoup
with request.urlopen('https://www.python.org/events/python-events/') as f:
    soup = BeautifulSoup(f, 'lxml', from_encoding='utf-8')
    fp = soup.section.text
    print((fp.split('More')[1]).split('You just missed...')[0])
