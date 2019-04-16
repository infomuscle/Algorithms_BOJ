# 문제
# 어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

N = int(input())

def findHansu(inNum):
    if inNum < 100 and inNum > 0:
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

count = 0
for i in range(N, 0, -1):
    if findHansu(i) != None:
        count += 1

print(count)