def bubble_sort1(l):
    print(l)
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
        print(l)
list=[23,1234,2,15,24,100,25,4]
bubble_sort1(list)

# L=[23,1234,2,15,24,100,25,4]
# for n in L:
#     print(n)
# for x in [5,2,9]:
#     print(x)