score = [0,0,0,0,0]

for i in range(0,len(score)):
    score[i] = int(input())
    if score[i] < 40:
        score[i] = 40

total = 0

for i in range(len(score)):
    total += score[i]

print(int(total/5))