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
        if (before == "(" or before == "[") and (ps[i-1] == ")" or ps[i-1] == "]") and (ps[i] == ")" or ps[i] == "]"):
            stack.pop()
            if ps[i] == ")":
                m = 2
            elif ps[i] == "]":
                m = 3
            if len(stack) == 0:
                t = 0
                for i in range(len(temp)):
                    t += temp.pop()
                t *= m
                temp.append(t)
            else:
                temp[len(temp)-1] *= m
        elif (before == "(" or before == "[") and (ps[i] == ")" or ps[i] == "]"):
            if ps[i] == ")":
                m = 2
            elif ps[i] == "]":
                m = 3
            stack.pop()
            temp.append(m)
        else:
            stack.append(ps[i])
        if len(stack) == 0:
            result += temp.pop()

    print(result)