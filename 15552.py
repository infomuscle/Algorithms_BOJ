import sys

testCase = int(input())

for i in range(0, testCase):
    numIn = sys.stdin.readline().rstrip()
    numList = numIn.split(" ")
    sum = int(numList[0]) + int(numList[1])
    print(sum)