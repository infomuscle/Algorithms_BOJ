# 문제
# 수 124를 뒤집으면 421이 되고 이 두 수를 합하면 545가 된다.
# 124와 같이 원래 수와 뒤집은 수를 합한 수가 좌우 대칭이 되는지 테스트 하는 프로그램을 작성하시오.

# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄에 하나의 정수 N(10 ≤ N ≤ 100000)이 주어진다.

# 출력
# 각 테스트 케이스에 대해서 원래 수와 뒤집은 수를 합한 수가 좌우 대칭이 되면 YES를 아니면 NO를 한 줄에 하나씩 출력한다.

import sys

tc = int(sys.stdin.readline())

for t in range(tc):
    num1 = sys.stdin.readline().rstrip()
    num2 = ""
    for i in range(len(num1)-1, -1, -1):
        num2 += num1[i]

    sum1 = str(int(num1) + int(num2))
    sum2 = ""
    for i in range(len(str(sum1))-1, -1, -1):
        sum2 += sum1[i]

    if sum1 == sum2:
        print("YES")
    else:
        print("NO")