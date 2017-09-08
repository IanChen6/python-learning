import sqlite3

conn = sqlite3.connect('test.db')#连接SQLite


cursor = conn.cursor()# 创建一个Cursor:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')#创建user表
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')#嵌入一条记录
print(cursor.rowcount)

cursor.close()
conn.commit()
conn.close()