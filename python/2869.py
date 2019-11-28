import sys

a, b, v = map(int, sys.stdin.readline().split())

height = 0
day = 1
while True:
    height += a
    if height >= v:
        break
    height -= b
    day += 1

print(day)