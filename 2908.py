samples = input().split()
tmp = ""
sangsuList = []

for i in range(0, 2):
    for j in range(0,3):
        tmp += samples[i][2-j]
    sangsuList.append(int(tmp))
    tmp = ""

if sangsuList[0] > sangsuList[1]:
    print(sangsuList[0])
elif sangsuList[0] < sangsuList[1]:
    print(sangsuList[1])