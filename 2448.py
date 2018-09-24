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