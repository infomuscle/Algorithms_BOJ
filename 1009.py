# 문제
# 재용이는 최신 컴퓨터 10대를 가지고 있다.
# 어느 날 재용이는 많은 데이터를 처리해야 될 일이 생겨서 각 컴퓨터에 1번부터 10번까지의 번호를 부여하고,
# 10대의 컴퓨터가 다음과 같은 방법으로 데이터들을 처리하기로 하였다.
# 1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터, 3번 데이터는 3번 컴퓨터, ... ,
# 10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터, 12번 데이터는 2번 컴퓨터, ...
# 총 데이터의 개수는 항상 ab개의 형태로 주어진다.
# 재용이는 문득 마지막 데이터가 처리될 컴퓨터의 번호가 궁금해졌다.
# 이를 수행해주는 프로그램을 작성하라.

# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트 케이스에 대해 정수 a와 b가 주어진다.
# (1 ≤ a < 100, 1 ≤ b < 1,000,000)

# 출력
# 각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터의 번호를 출력한다.

import sys

mods0 = [10]
mods1 = [1]
mods2 = [2,4,8,6]
mods3 = [3,9,7,1]
mods4 = [4,6]
mods5 = [5]
mods6 = [6]
mods7 = [7,9,3,1]
mods8 = [8,4,2,6]
mods9 = [9,1]
mods = [mods0, mods1, mods2, mods3, mods4, mods5, mods6, mods7, mods8, mods9]

tc = int(sys.stdin.readline())

for t in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    lastNum = a%10
    if lastNum == 0 or lastNum == 1 or lastNum == 5 or lastNum == 6:
        print(mods[lastNum][0])
    elif lastNum == 4 or lastNum == 9:
        if b%2 == 0:
            print(mods[lastNum][1])
        else:
            print(mods[lastNum][0])
    elif lastNum == 2 or lastNum == 3 or lastNum == 7 or lastNum == 8:
        idx = b%4
        print(mods[lastNum][idx-1])