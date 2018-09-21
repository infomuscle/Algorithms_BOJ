import sys

most = 0
train = 0

for i in range(4):
    off, on = map(int, sys.stdin.readline().split())
    train -= off
    train += on
    if train > most:
        most = train

print(most)