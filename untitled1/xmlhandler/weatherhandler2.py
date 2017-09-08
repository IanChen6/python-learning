from xml.parsers.expat import ParserCreate
from datetime import datetime, timedelta

class DefaultSaxHandler(object):
    def __init__(self):
        self.today = datetime.now().strftime('%a')
        self.tomorrow = (datetime.now() + timedelta(days=1)).strftime('%a')
        self.__data = {
            'city':'',
            'country': '',
            'today': {
                'text': '',
                'low': 0,
                'high': 0,
            },
            'tomorrow': {
                'text': '',
                'low': 0,
                'high': 0
            }
        }

    @property
    def get_data(self):
        return self.__data

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.__data['city'] = attrs['city']
            self.__data['country'] = attrs['country']
        if name == 'yweather:forecast':
            if attrs['day'] == self.today:
                self.__data['today']['text'] = attrs['text']
                self.__data['today']['low'] = attrs['low']
                self.__data['today']['high'] = attrs['high']
            if attrs['day'] == self.tomorrow:
                self.__data['tomorrow']['text'] = attrs['text']
                self.__data['tomorrow']['low'] = attrs['low']
                self.__data['tomorrow']['high'] = attrs['high']

    def end_element(self, name, attrs):
        pass

    def char_data(self, text):
        pass

data = 'your data'

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(data)

print(handler.get_data)
