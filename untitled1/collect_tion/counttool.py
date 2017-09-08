from collections import Counter
c=Counter()
with open("D:\word.txt",encoding='utf8') as f:
    txt=f.read()
    for ch in txt:
        c[ch]=c[ch]+1
    print(c)