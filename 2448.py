# 문제
# 예제를 보고 별찍는 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N이 주어진다. N은 항상 3*2^k 수이다. (3, 6, 12, 24, 48, ...) (k<=10)

# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.

import sys
import math

lines = []

def starAdder(n, idx):
    stars = ["*", "* *", "*****"]
    k = round(math.log(n, 2) - math.log(3, 2))

    if idx == 0:
        for i in range(3):
            lines.append(stars[i])
    else:
        start = 6*(2**(idx-1))-1
        for i in range(0, len(lines)):
            space = " "*(start-2*i)
            s = lines[i] + space + lines[i]
            lines.append(s)

    if idx == k:
        return
    starAdder(n, idx+1)

n = int(sys.stdin.readline())
k = round(math.log(n, 2) - math.log(3, 2))
length = 6*(2**k)-1

starAdder(n, 0)

for i in range(0, len(lines)):
    ll = lines[i].center(length, " ")
    print(ll)