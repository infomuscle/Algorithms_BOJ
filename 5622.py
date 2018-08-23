time = [11,2,3,4,5,6,7,8,9,10]
ch = [[],[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

word = input()
callNum = ""
callTime = 0

for i in range(0, len(word)):
    for j in range(0,len(ch)):
        if word[i] in ch[j]:
            callNum += str(j)

for i in range(0,len(callNum)):
    callTime += time[int(callNum[i])]

print(callTime)