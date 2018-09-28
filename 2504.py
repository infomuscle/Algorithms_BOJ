import sys

def vpsChecker(ps):
    flag = 1
    stack = []

    for i in range(0, len(ps)):
        if ps[i] == "(":
            stack.append(1)
        elif ps[i] == ")":
            if len(stack) == 0:
                flag = 0
                break
            else:
                stack.pop()

    if len(stack) != 0:
        flag = 0

    if flag == 1:
        return True
    else:
        return False

ps = sys.stdin.readline().rstrip()
stack = []
sum = 0

temp = 0

if vpsChecker(ps) == True:
    for i in range(len(ps)):
        stack.append(ps[i])

    for i in range(len(ps)-1, -1, -1):
        if ps[i] == ")":
            if temp == 0:
                temp = 2
            else:
                temp *= 2
        elif ps[i] == "]":
            if temp == 0:
                temp = 3
            else:
                temp *= 3
        elif ps[i] == "[" or ps[i] == "(":
            sum += temp
            temp = 0
    print(sum)

else:
    print(0)