def solution(N, house):
    answer = 0

    factory = []
    for i in range(-100, 101):
            for j in range(-100, 101):
                factory.append([i, j])

    distanceList = []
    for h in range(0, len(house)):
        distance = 0
        for f in range(0, len(factory)):
            temp = ((house[h][0]-factory[f][0])**2) + ((house[h][1]-factory[f][1])**2)
            if temp >= distance:
                distance = temp
                distanceList.append(distance)
    distanceList.sort()
    answer = distanceList[0]
    return answer

n1 = 1
h1 = [[0,0]]
n2 = 3
h2 = [[0,0],[1,0]]

print(solution(n2, h2))