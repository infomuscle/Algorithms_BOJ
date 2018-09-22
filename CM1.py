def solution(people, tshirts):
    answer = 0
    for i in range(1, 1001):
        p = people.count(i)
        t = tshirts.count(i)
        if p == 0 or t == 0:
            pass
        elif p >= t:
            answer += t
        elif p < t:
            answer += p

    return answer


p1 = [2,3]
t1 = [1,2,3]
p2 = [1,2,3]
t2 = [1,1]

print(solution(p1, t1))
print(solution(p2, t2))