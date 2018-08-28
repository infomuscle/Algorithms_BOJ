cAlpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

inStr = input()

for i in range(len(inStr)):
    count += 1
    if i == len(inStr) - 1:
        break

    if inStr[i] == "c" and inStr[i+1] == "=":
        count -= 1
    elif inStr[i] == "c" and inStr[i+1] == "-":
        count -= 1
    elif inStr[i] == "d" and inStr[i+1] == "z" and inStr[i+2] == "=":
        count -= 1
    elif inStr[i] == "d" and inStr[i+1] == "-":
        count -= 1
    elif inStr[i] == "l" and inStr[i+1] == "j":
        count -= 1
    elif inStr[i] == "n" and inStr[i+1] == "j":
        count -= 1
    elif inStr[i] == "s" and inStr[i+1] == "=":
        count -= 1
    elif inStr[i] == "z" and inStr[i+1] == "=":
        count -= 1

print(count)