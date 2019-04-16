# 문제
# 겨울 방학에 달에 다녀온 상근이는 여름 방학 때는 화성에 갔다 올 예정이다. (3996번)
# 화성에서는 지구와는 조금 다른 연산자 @, %, #을 사용한다. @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다.
# 따라서, 화성에서는 수학 식의 가장 앞에 수가 하나 있고, 그 다음에는 연산자가 있다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 다음 줄에는 화성 수학식이 한 줄에 하나씩 주어진다.
# 수학식은 100자를 넘지 않는다.

# 출력
# 각 테스트 케이스에 대해서, 화성 수학식의 결과를 계산한 다음에, 소수점 둘째 자리까지 출력한다.

import sys

tc = int(sys.stdin.readline())
box = []
num = None

for t in range(tc):
    box = sys.stdin.readline().split()
    num = float(box[0])
    for i in range(len(box)-1):
        if box[i+1] == "@":
            num *= 3
        elif box[i+1] == "%":
            num += 5
        elif box[i+1] == "#":
            num -=7
    print("%.2f" % num)