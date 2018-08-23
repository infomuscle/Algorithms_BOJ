c0,c1,c2,c3,c4,c5,c6,c7,c8,c9 = 0,0,0,0,0,0,0,0,0,0
cList = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]

n1 = int(input())
n2 = int(input())
n3 = int(input())

num = str(n1*n2*n3)

for i in range(0,10):
    for j in range(0,len(num)):
        if str(i) == num[j]:
            cList[i] += 1
    print(cList[i])