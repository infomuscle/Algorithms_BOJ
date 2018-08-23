ch = input().upper()
countList, original = [], []

for i in range(65, 91):
    countList.append(ch.count(chr(i)))

for i in range(0, len(countList)):
    original.append(countList[i])

countList.sort()
countList.reverse()
bgst = countList[0]

if countList[0] == countList[1]:
    print("?")
else:
    print(chr(original.index(bgst)+65))