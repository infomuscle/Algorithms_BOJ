food_times = [3,1,2]
k = 1

def idxAdder(idx, foods):
    if idx+1 == foods:
        result = 0
    else:
        result = idx+1
    return result

def solution(food_times, k):
    timer, idx = 0,0
    foods = len(food_times)

    while True:
        if food_times[idx] != 0:
            food_times[idx] -= 1
            timer += 1
            idx = idxAdder(idx, foods)
            if timer == k:
                while True:
                    if food_times[idx] != 0:
                        answer = idx + 1
                        break
                    else:
                        idx = idxAdder(idx, foods)
                break
            elif timer > k:
                answer = -1
                break
        else:
            idx = idxAdder(idx, foods)


    return answer

print(solution(food_times,k))

# if idx + 1 == foods:
#     idx = 0
# else:
#     idx += 1