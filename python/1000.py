# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력1
# 첫째 줄에 A+B를 출력한다.

import sys

num1, num2 = map(int, sys.stdin.readline().split())

print(num1 + num2)