import sys

N = int(sys.stdin.readline())
stages = list(map(int, sys.stdin.readline().split()))

staysList = [0]*(N+1)
reachesList = [0]*(N+1)

for i in range(0,len(stages)):
    for j in range(N+1, 0, -1):
        if stages[i] == j:
            for k in range(0, j):
                reachesList[k] += 1
            staysList[j-1] += 1

failRateList = [0] * (N)
for i in range(0, N):
    if reachesList[i] == 0:
        failRateList[i] = 0
    else:
        failRateList[i] = staysList[i] / reachesList[i]

rateSorted = sorted(failRateList)
rateSorted.reverse()

print(failRateList)

answer = []
for i in range(0, N):
    for j in range(0,N):
        if rateSorted[i] == failRateList[j]:
            answer.append(j+1)
            failRateList[j] = 2

print(staysList)
print(reachesList)
print(answer)
