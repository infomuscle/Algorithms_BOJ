import sys

x, y, w, h = map(int, sys.stdin.readline().split())

dists = [x, w-x, y, h-y]
dists.sort()
print(dists[0])