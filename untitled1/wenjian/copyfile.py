with open("D:\word.txt","r",encoding='utf-8') as f:
        sr = f.read()
with open("D:\word.txt", "a", encoding='utf-8') as f:
        for i in range(10):
            f.write(sr)
