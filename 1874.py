import sys

stack, printBox = [], []
top, num = 0,0

def topper(cmd, top):
    if cmd == "add":
        top += 1
        if top > 7:
            top = 7
    elif cmd == "sub":
        top -= 1
        if top < 0:
            top = 0
    return top

n = int(sys.stdin.readline())

for i in range(0, n):
    k = int(sys.stdin.readline())
    if len(stack) == 0:
        num += 1
        stack.append(num)
        printBox.append("+")
        top = topper("add", top)
        if stack[top-1] == k:
            stack.pop()
            printBox.append("-")
            top = topper("sub", top)
        else:
            while stack[top-1] != k:
                num += 1
                stack.append(num)
                printBox.append("+")
                top = topper("add", top)
            stack.pop()
            printBox.append("-")
            top = topper("sub", top)
    elif stack[top-1] < k:
        while stack[top-1] != k:
            num += 1
            stack.append(num)
            printBox.append("+")
            top = topper("add", top)
        stack.pop()
        printBox.append("-")
        top = topper("sub", top)
    elif stack[top-1] == k:
        stack.pop()
        printBox.append("-")
        top = topper("sub", top)
    else:
        printBox.append("NO")

if "NO" in printBox:
    print("NO")
else:
    for i in range(len(printBox)):
        print(printBox[i])