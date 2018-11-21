# 문제
# 상근이는 길을 걷다가 신기한 기계를 발견했다.
# 기계는 매우 매우 큰 화면과 버튼 하나로 이루어져 있다.
# 기계를 발견했을 때, 화면에는 A만 표시되어져 있었다. 버튼을 누르니 글자가 B로 변했다.
# 한 번 더 누르니 BA로 바뀌고, 그 다음에는 BAB, 그리고 BABBA로 바뀌었다.
# 상근이는 화면의 모든 B는 BA로 바뀌고, A는 B로 바뀐다는 사실을 알게되었다.
# 버튼을 K번 눌렀을 때, 화면에 A와 B의 개수는 몇 개가 될까?

# 입력
# 첫째 줄에 K (1 ≤ K ≤ 45)가 주어진다.

# 출력
# 첫째 줄에 A의 개수와 B의 개수를 공백으로 구분해 출력한다.

import sys

fibs = [0, 1]

for i in range(44):
    fibs.append(fibs[-1] + fibs[-2])

n = int(sys.stdin.readline())
print("%d %d" % (fibs[n-1], fibs[n]))