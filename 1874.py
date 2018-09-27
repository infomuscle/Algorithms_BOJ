import sys

stack, printBox = [], []
top, num = 0,0
flag = 1

n = int(sys.stdin.readline())

for i in range(0, n):
    k = int(sys.stdin.readline())
    if len(stack) == 0:
        num += 1
        stack.append(num)
        printBox.append(1)
        top += 1
        if stack[top-1] == k:
            stack.pop()
            printBox.append(0)
            top -= 1
        else:
            while stack[top-1] != k:
                num += 1
                stack.append(num)
                printBox.append(1)
                top += 1
            stack.pop()
            printBox.append(0)
            top -= 1
    elif stack[top-1] < k:
        while stack[top-1] != k:
            num += 1
            stack.append(num)
            printBox.append(1)
            top += 1
        stack.pop()
        printBox.append(0)
        top -= 1
    elif stack[top-1] == k:
        stack.pop()
        printBox.append(0)
        top -= 1
    else:
        flag = 0

if flag == 0:
    print("NO")
else:
    for i in range(0, len(printBox)):
        if printBox[i] == 1:
            print("+")
        else:
            print("-")