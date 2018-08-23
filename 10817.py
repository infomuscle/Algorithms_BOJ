numSet = input().split(" ")
for i in range(0, len(numSet)):
    numSet[i] = int(numSet[i])
numSet.sort()
print(numSet[1])