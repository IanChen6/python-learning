# try:
#     print('try division')
#     def fun(a):
#         return int(100/a)
#     print('result:',fun(1))
# except ZeroDivisionError as e:#无错误发生时except不执行，finall仍会执行
#     print('except:',e)
# finally:
#     print('finally')
# print("end")
# #多个except来捕获不同类型的错误;如果没有错误发生，可以在except语句块后面加一个else，
# # 当没有错误发生时，会自动执行else语句：
# try:
#     print('try...')
#     r = 10 / int('a')
#     # r = 10 / int('12')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('No error')
# finally:
#     print('finally...')
# print('END')
# #错误其实也是class，所有的错误类型都继承自BaseException，
# # 所以在使用except时需要注意的是，它不但捕获该类型的错误，
# # 还把其子类也“一网打尽”
# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')
 #第二个except永远也捕获不到UnicodeError，
# 因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了

#自定义错误类型
class Ferror(ValueError):
    pass
def f(s):
    n=int(s)
    if n==0:
        raise Ferror("invalid value:&s"% n)
    return 10/n
f('0')