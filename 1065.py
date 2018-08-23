N = int(input())

def findHansu(inNum):
    if inNum <100:
        return inNum
    else:
        numList = []
        inNumStr = str(inNum)
        for i in range(0, len(inNumStr)):
            numList.append(inNumStr[i])
        for i in range(0, len(numList)):
            numList[i] = int(numList[i])
        if numList[0]-numList[1] == numList[1] - numList[2]:
            return inNum

for i in range(N, 0, -1):
    if findHansu(i) != None:
        print(findHansu(i))
        break