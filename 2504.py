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
        print("YES")
    else:
        print("NO")
