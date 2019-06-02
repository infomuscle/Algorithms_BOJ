import sys

n, m = map(int, sys.stdin.readline().split())

cnt = 0

while n/m != 0:
    cnt += n
    n //= m

print(cnt)