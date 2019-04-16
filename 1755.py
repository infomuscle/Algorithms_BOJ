# 문제
# 79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다.
# 80은 마찬가지로 "eight zero"라고 읽는다.
# 79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.
# 문제는 정수 M, N(1 ≤ M, N ≤ 99)이 주어지면
# M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.

# 입력
# 첫째 줄에 M과 N이 주어진다.

# 출력
# M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.

import sys

numIndex1 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 0:"zero"}
numIndex2 = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
readNums = []

start, end = map(int, sys.stdin.readline().split())
for i in range(start, end+1):
    temp = ""
    for x in str(i):
        temp += numIndex1[int(x)] + " "
    temp = temp.strip()
    readNums.append(temp)

readNums.sort()

idx = 0
for x in readNums:
    tempList = x.split()
    for y in tempList:
        print(numIndex2[y], end="")
    print(" ", end = "")
    idx += 1
    if idx == 10:
        idx = 0
        print("")