# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1≤M≤N≤1,000,000)

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

import sys

m, n = map(int, sys.stdin.readline().split())
primes = []

for i in range(m, n+1):
    if i == 1:
        continue
    elif i == 2:
        print(i)
    else:
        end = int(i**0.5)+1
        flag = 1
        for j in range(2, end+1):
            if i%j == 0:
                flag = 0
                break
        if flag == 1:
            print(i)