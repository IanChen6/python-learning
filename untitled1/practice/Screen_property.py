class Screen(object):
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError("width must be an integer")
        self.__width=value
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        self.__height = value
    @property
    def resolution(self):
        self.__resolution=self.__width*self.__height
        return self.__resolution
s=Screen()
s.width=1024
s.height=768
print(s.resolution)
assert s.resolution==786432,"1024*768=%d ?"%s.resolution#assert用于断言，若为FALSE则返回后面的信息