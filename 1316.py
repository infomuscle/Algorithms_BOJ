tc = int(input())
count = 0

def groupChecker(inWord):
    chBox = []
    chBox.append(inWord[0])
    for i in range(1, len(inWord)):
        if inWord[i] != inWord[i-1] and inWord[i] in chBox:
            return False
        else:
            chBox.append(inWord[i])
    return True

for i in range(0, tc):
    word = input()
    if groupChecker(word) == True:
        count += 1

print(count)