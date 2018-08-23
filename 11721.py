wordIn = input()
wordOut = ""

for i in wordIn:
    wordOut += i
    if len(wordOut)%10 == 0:
        print(wordOut)
        wordOut = ""

print(wordOut)