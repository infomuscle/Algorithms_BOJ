import sys

tc = int(sys.stdin.readline())

for t in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    num = 0
    while True:
        if a > b:
            num += a
            if num%b == 0:
                break
        else:
            num += b
            if num%a == 0:
                break
    print(num)