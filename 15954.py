import sys
import math

n, k = map(int, sys.stdin.readline().split())
likes = list(map(int, sys.stdin.readline().split()))

def varFinder(l):
    sqrSum, sum = 0, 0
    for i in range(len(l)):
        sqrSum += l[i]**2
        sum += l[i]
    var = sqrSum/len(l) - (sum/len(l))**2
    return var

small = 0

for i in range(k, len(likes)+1):
    for j in range(0, len(likes)-i+1):
        nowVar = varFinder(likes[j:j+i])
        if i == k and j == 0:
            small = nowVar
        elif small > nowVar:
            small = nowVar

print(math.sqrt(small))