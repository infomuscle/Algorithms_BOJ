# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

import sys

n = int(sys.stdin.readline())
leng = 2*n-1

for i in range(n):
    star = "*" * (2*(i+1)-1)
    space = " " * (n-(i+1))
    print(space, end="")
    print(star)

for i in range(n-2,-1,-1):
    star = "*" * (2*(i+1)-1)
    space = " " * (n-(i+1))
    print(space, end="")
    print(star)