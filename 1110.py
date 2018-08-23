startNum = input()
numList = []
cycle = 0

if int(startNum)<=9:
    numList.append("0")

for i in startNum:
    numList.append(i)
for i in range(0, len(numList)):
    numList[i] = int(numList[i])

while True:
    newNum = (numList[0] + numList[1])%10
    numList[0] = numList[1]
    numList[1] = newNum
    cycle += 1
    if int(startNum) <= 9:
        if str(numList[0])=="0" and startNum==str(newNum):
            break
    else:
        if startNum == str(numList[0]) + str(newNum):
            break
print(cycle)