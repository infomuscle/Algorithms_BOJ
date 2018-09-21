import sys

def stickAdder(x, stick, cnt, idx):
    unit = [64, 32, 16, 8, 4, 2, 1]
    if stick+unit[idx] == x:
        print(cnt)
    elif stick+unit[idx] < x:
        stick += unit[idx]
        stickAdder(x, stick, cnt+1, idx+1)
    else:
        stickAdder(x, stick, cnt, idx+1)

x = int(sys.stdin.readline())

stickAdder(x,0,1,0)