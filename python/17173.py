import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
added = []

sum = 0
for x in nums:
    c = x
    while c <= n:
        if c not in added:
            sum += c
            added.append(c)
        c += x

print(sum)