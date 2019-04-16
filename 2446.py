# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

import sys

n = int(sys.stdin.readline())

for i in range(n,0,-1):
    star = "*" * (2*i-1)
    space = " " * (n-i)
    print(space, end="")
    print(star)

for i in range(1,n):
    star = "*" * (2*i+1)
    space = " " * (n-1-i)
    print(space, end="")
    print(star)