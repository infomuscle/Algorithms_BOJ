# 문제
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

import sys

num1 = sys.stdin.readline().strip()
num2 = sys.stdin.readline().strip()


num1 = num1[::-1]
num2 = num2[::-1]

answers = []

tot = 0
multiplier2 = 1
for x in num2:
    answer = 0
    multiplier1 = 1
    for y in num1:
        answer += int(y) * int(x) * multiplier1
        multiplier1 *= 10
    tot += answer * multiplier2
    answers.append(answer)
    multiplier2 *= 10
answers.append(tot)


for a in answers:
    print(a)