# 나누기 풀이 중

import sys

n = int(sys.stdin.readline())
f = int(sys.stdin.readline())

for i in range(2):
    n /= 10
n *= 100

while True:
    if n%f == 0:
        break
    else:
        n += 1

n2 = n%10
n1 = (n%100)/10

print(n1, end="")
print(n2)