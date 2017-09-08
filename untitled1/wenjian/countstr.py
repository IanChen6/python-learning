
# with open("D:\word.txt") as f:
with open("D:\word.txt",encoding='utf-8') as f:
    s = f.read()
    # 这里的s采用文件的方式读取
global list_all#存储字符（不重复）
global list_to_statistic#存储次数


def tran_s_to_list(s):
    list_all = []
    l = len(s)
    # 得到长度，遍历
    for x in range(0, l):
        # 当x不在list中，即第一次出现，追加到list中
        if not s[x] in list_all:
            list_all.append(s[x])
    return list_all


def statistic(s, list_all, list_to_statistic):
    l = len(s)
    for x in range(0, l):
        #遍历字符串，找到每一个char在list中的index，在list_statistic相应位置加一
        list_to_statistic[list_all.index(s[x])] = list_to_statistic[list_all.index(s[x])] + 1
        # print list_all.index(s[x]),
        # print


list_all = tran_s_to_list(s)
# 复制一个和list等长的数组list_statistic，并且全部赋值为0
list_to_statistic = list_all[:]
for x in range(0, len(list_all)):
    list_to_statistic[x] = 0

statistic(s, list_all, list_to_statistic);
# 打印
listlength = len(list_all)
for x in range(0, listlength):
    print(str(list_all[x]) + "" + "---appears---" + str(list_to_statistic[x]) + "---times")
