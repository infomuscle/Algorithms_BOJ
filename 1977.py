import sys
import math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

pRoot = math.ceil(math.sqrt(m))
pList = []
sum = 0
while pRoot*pRoot <= n:
    pList.append(pRoot*pRoot)
    sum += pRoot*pRoot
    pRoot += 1

if len(pList) == 0:
    print(-1)
else:
    print(sum)
    print(pList[0])