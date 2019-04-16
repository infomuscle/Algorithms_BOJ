# 문제
# 키파는 곱하기를 좋아한다.
# 그래서 키파는 수를 보면 각 자리 숫자를 모두 곱해서 하나의 수를 만든다.
# 키파는 기쁘다.
# 키파는 이 작업을 계속해서 반복한다.
# 그런데 수가 한 자리가 되었다.
# 키파는 슬퍼졌다.
# 키파의 기쁨이 지속될 수 있는 것이 몇 단계인지를 출력하는 프로그램을 작성하시오.
# 예를 들어 679라면:
# 679 → 6*7*9 = 378 (1단계)
# 378 → 3*7*8 = 168 (2단계)
# 168 → 1*6*8 = 48 (3단계)
# 48 → 4*8 = 32 (4단계)
# 32 → 3*2 = 6 (5단계: 키파는 슬퍼졌다.)
# 키파는 5단계만에 슬퍼지므로 5를 출력하면 된다.

# 입력
# 각각의 입력은 하나의 테스트 케이스로 이루어진다.
# 입력은 첫 번째 줄에 선행하는 0이 없는 9자리 이하의 수가 하나 주어진다.

# 출력
# 각각의 입력에 대해 키파의 기쁨이 지속될 수 있는 단계의 수를 출력하라.

import sys

n = sys.stdin.readline().rstrip()
cnt = 0

while True:
    if len(n) == 1:
        break
    else:
        cnt += 1
        temp = 1
        for i in range(len(n)):
            temp *= int(n[i])
        n = str(temp)

print(cnt)