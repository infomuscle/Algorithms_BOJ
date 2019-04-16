# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

import sys

n = int(sys.stdin.readline())

for i in range(n):
    frontSpace = " " * (n-(i+1))
    if i == 0:
        print(frontSpace, end="")
        print("*")
    else:
        middleSpace = " " * (2*i-1)
        print(frontSpace, end="")
        print("*", end='')
        print(middleSpace, end="")
        print("*")