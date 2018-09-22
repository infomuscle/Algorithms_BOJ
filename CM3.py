from itertools import permutations

def solution(healths, items):
    answer = []
    maxAttack = 0
    healthsOrder = list(permutations(healths, len(healths)))

    for h in healthsOrder:
        temp = 0
        tempList = []
        for i in range(0, len(h)):
            if h[i]-items[i][1] >= 100:
                temp += items[i][0]
                tempList.append(i+1)
        if temp > maxAttack:
            maxAttack = temp
            answer = tempList

    return answer


h1 = [200,120,150]
i1 = [[30,100],[500,30],[100,400]]
h2 = [300,200,500]
i2 = [[1000, 600], [400, 500], [300, 100]]

print(solution(h1, i1))
print(solution(h2, i2))