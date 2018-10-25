import sys

def vpsChecker(ps):
    stack = []
    for i in range(0, len(ps)):
        if len(stack) == 0:
            stack.append(ps[i])
            continue
        before = stack[len(stack)-1]
        if before == "[" and ps[i] == "]":
            stack.pop()
        elif before == "(" and ps[i] == ")":
            stack.pop()
        else:
            stack.append(ps[i])

    if len(stack) == 0:
        return True
    else:
        return False

ps = sys.stdin.readline().rstrip()

if vpsChecker(ps) == False:
    print(0)
else:
    result = 0
    temp = []
    stack = []

    for i in range(0, len(ps)):
        if len(stack) == 0:
            stack.append(ps[i])
            continue
        before = stack[len(stack)-1]
        if before == "(" and ps[i-1] == ")" and ps[i] == ")":
            stack.pop()
            if len(stack) == 0:
                t = 0
                for i in range(len(temp)):
                    t += temp.pop()
                t *= 2
                temp.append(t)
            else:
                temp[len(temp)-1] *= 2
        elif before == "(" and ps[i] == ")":
            stack.pop()
            temp.append(2)
        else:
            stack.append(ps[i])
        if len(stack) == 0:
            result += temp.pop()

    print(result)