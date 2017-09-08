import functools
def log(text):
    def decoration(func):
        @functools.wraps(func)#在wrapper函数前使用
        def wrapper(*args,**kw):
            if text!=None:
                print('%s begin call %s():' % (text, func.__name__))
                return func
                print('%s end call %s():' % (text, func.__name__))
            else:
                print('begin call %s():' % (func.__name__))
                return func
                print('end call %s():' % (func.__name__))
        return wrapper
    if isinstance(text,str):
        return decoration
    else:
        strtmp = text
        text = None
        return decoration(strtmp)#有疑问
@log
def now():
    print("123456")
now()



