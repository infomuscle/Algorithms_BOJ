import sys

def vpsChecker(ps):
    flag = 1
    stack = []
    before = ""

    for i in range(0, len(ps)):
        if len(stack) == 0 and (ps[i] == "]" or ps[i] == ")"):
            flag = 0
            break
        else:
            if ps[i] == "(":
                stack.append(ps[i])
            elif ps[i] == ")":
                if before == "[":
                    flag = 0
                    break
                else:
                    stack.pop()
            elif ps[i] == "[":
                stack.append(ps[i])
            elif ps[i] == "]":
                if before == "(":
                    flag = 0
                    break
                else:
                    stack.pop()
            before = ps[i]
    if len(stack) != 0:
        flag = 0

    if flag == 1:
        return True
    else:
        return False

ps = sys.stdin.readline().rstrip()
stack1 = []
stack2 = []
sum = 0
before = ""

if vpsChecker(ps) == True:
    for i in range(len(ps)):
        if ps[i] == "(":
            stack1.append(2)
        elif ps[i] == ")":
            a = stack1.pop()
            if len(stack1) == 0:
                if len(stack2) == 0:
                    sum += a
                else:
                    temp = 0
                    for j in range(0, len(stack2)):
                        temp += stack2[j]
                    sum += a*temp
                    stack2 = []
            elif before == ")" or before == "]":
                b = stack2.pop()
                stack2.append(a*b)
            else:
                stack2.append(a)
        elif ps[i] == "[":
            stack1.append(3)
        elif ps[i] == "]":
            a = stack1.pop()
            if len(stack1) == 0:
                if len(stack2) == 0:
                    sum += a
                else:
                    temp = 0
                    for j in range(0, len(stack2)):
                        temp += stack2[j]
                    sum += a * temp
                    stack2 = []
            elif before == ")" or before == "]":
                b = stack2.pop()
                stack2.append(a*b)
            else:
                stack2.append(a)
        before = ps[i]

    print(sum)

else:
    print(0)