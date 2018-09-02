import sys
import math

n, k = map(int, sys.stdin.readline().split())
likes = list(map(int, sys.stdin.readline().split()))

def avgFinder(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum/len(l)

def varFinder(l):
    sum = 0
    avg = avgFinder(l)
    for i in range(len(l)):
        sum += (l[i]-avg)**2
    return sum/len(l)

# def sdFinder(l):
#     return math.sqrt(varFinder(l))

# temp = []
# sd = 0
varList = []

# for i in range(k, len(likes)+1):
#     temp = [0] * i
#     for h in range(0, len(likes) - i + 1):
#         for j in range(0, i):
#             temp[j] = likes[j + h]
#         sdList.append(varFinder(temp))

for i in range(k, len(likes)+1):
    for j in range(0, len(likes)-i+1):
        varList.append(varFinder(likes[j:j+i]))

    # a[0:0+k] a[0:0+k]
    # a[1:1+k] a[1:1+k]
    # a[2:2+k]

varList.sort()

print(math.sqrt(varList[0]))

        # if i == k and h == 0:
        #     sd = sdFinder(temp)
        # elif sd > sdFinder(temp):
        #     sd = sdFinder(temp)

# print(sd)