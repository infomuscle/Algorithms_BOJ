weight = int(input())

# 10, 15, 20, 25, ... 3 = 0, 5 = 2,3,4,5,6,7
list0 = []

# 8, 13, 18, 23, ... 3 = 1, 5 = 1,2,3,4,5,6
list1 = []

# 11, 16, 21, 26, ... 3 = 2, 5 = 1,2,3,4,5,6
list2 = []

# 9, 14, 19, 24, ... 3 = 3, 5 = 0,1,2,3,4,5
list3 = []

# 12, 17, 22, 27, ... 3 = 4, 5 = 0,1,2,3,4,5
list4 = []

for i in range(2, 1001):
    a = i*5
    list0.append(a)

for i in range(1, 1000):
    b = 3*1 + i*5
    list1.append(b)

for i in range(1, 999):
    c = 3*2 + i*5
    list2.append(c)

for i in range(0, 999):
    d = 3*3 + i*5
    list3.append(d)

for i in range(0, 998):
    e = 3*4 + i*5
    list4.append(e)

if weight == 3 or weight == 5:
    print(1)
elif weight == 6:
    print(2)
elif weight == 4 or weight == 7:
    print(-1)
else:
    if weight in list0:
        aa = list0.index(weight)
        print(aa+2)
    elif weight in list1:
        bb = list1.index(weight)
        print(bb+1+1)
    elif weight in list2:
        cc = list2.index(weight)
        print(cc+1+2)
    elif weight in list3:
        dd = list3.index(weight)
        print(dd+3)
    elif weight in list4:
        ee = list4.index(weight)
        print(ee+4)
    else:
        print("ERROR")