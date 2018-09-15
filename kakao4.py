food_times = [3,1,2]
k = 1

def noFoodChecker(food_times):
    flag = 1
    for i in range(len(food_times)):
        if food_times[i] != 0:
            flag = 0
    return flag

def solution(food_times, k):
    timer, idx = 0,0
    foods = len(food_times)
    total_time = 0
    for i in range(foods):
        total_time += food_times[i]

    while True:
        if food_times[idx] != 0:
            food_times[idx] -= 1
            timer += 1
            if idx + 1 == foods:
                idx = 0
            else:
                idx += 1

            if timer > k:
                answer = -1
                break
            elif timer == k:
                while True:
                    if food_times[idx] == 0:
                        if idx + 1 == foods:
                            idx = 0
                        else:
                            idx += 1
                    else:
                        answer = idx + 1
                        break
                break
        else:
            if  timer == total_time:
                answer = -1
                break
            else:
                if idx + 1 == foods:
                    idx = 0
                else:
                    idx += 1

    return answer

print(solution(food_times,k))