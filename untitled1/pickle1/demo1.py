import pickle
d=dict(name="bob",age=20,score=90)
pickle.dumps(d)#dumps()方法把任意对象序列化成一个bytes，
print(pickle.dumps(d))
# 然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()
# 直接把对象序列化后写入一个file-like Object
f=open("D:\pydemo\序列化.txt",'wb')
pickle.dump(d,f)
f.close()
#当我们要把对象从磁盘读到内存时，
# 可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
f2=open("D:\pydemo\序列化.txt",'rb')
d2=pickle.load(f2)
f.close()
print(d2)