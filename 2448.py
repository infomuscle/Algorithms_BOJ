# 문제
# 예제를 보고 별찍는 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N이 주어진다. N은 항상 3*2^k 수이다.
# (3, 6, 12, 24, 48, ...) (k<=10)

# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.

# n = 3,6,12,24,48
# 5, 11, 23, 47

import sys

lines = []

def starPrinter(n, k):
    stars = ["*", "* *", "*****"]

    s = " "*(n-k) + stars[k-1] + " "*(n-k)
    lines.append(s)

    if k == n:
        for i in range(0, n):
            print(lines[i])
        return
    starPrinter(n, k+1)


n = int(sys.stdin.readline())

starPrinter(n, 1)