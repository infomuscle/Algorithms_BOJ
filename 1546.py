n = int(input())
scores = input().split()
for i in range(0, len(scores)):
    scores[i] = int(scores[i])

scores.sort()
m = scores[len(scores)-1]

newScores = []
for i in range(0, len(scores)):
    newScores.append(scores[i]/m*100)
total = 0
for i in range(0, len(newScores)):
    total += newScores[i]

avg = total/len(newScores)
print(avg)
