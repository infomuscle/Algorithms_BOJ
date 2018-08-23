tc = int(input())
tcList = [""]*tc
tcScore = [0]*tc

for i in range(0,tc):
    tcList[i] = input()
    score = 0
    for j in range(0, len(tcList[i])):
        if tcList[i][j] == "O":
            score += 1
            tcScore[i] += score
        else:
            score = 0
    print(tcScore[i])