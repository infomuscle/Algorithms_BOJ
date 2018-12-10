# 문제
# 최백준이 이번 학기에 들은 과목과 학점 그리고 성적이 주어졌을 때,
# 평균 평점을 계산하는 프로그램을 작성하시오.
# 성적은 A+~F까지 총 13개가 있다.
# A+: 4.3, A0: 4.0, A-: 3.7
# B+: 3.3, B0: 3.0, B-: 2.7
# C+: 2.3, C0: 2.0, C-: 1.7
# D+: 1.3, D0: 1.0, D-: 0.7
# F: 0.0
# 평균 평점은 각 과목의 학점*성적을 모두 더한 뒤에, 총 학점으로 나누면 된다.

# 입력
# 첫째 줄에, 백준이가 이번 학기에 들은 과목 수가 주어진다.
# 둘째 줄부터 N개의 줄에 각 과목의 과목명, 학점, 성적이 주어진다.
# 과목명은 알파벳 소문자와 숫자, 그리고 밑줄 (_)로만 이루어져 있으며, 최대 100글자이고,
# 학점은 1보다 크거나 같고, 3보다 작거나 같은 자연수이다.
# 성적은 문제에 설명한 13가지 중 하나이다.

# 출력
# 첫째 줄에 평균 평점을 소수점 셋째 자리에서 반올림해서 둘째 자리까지 출력한다.
# (평균 평점이 1.5이면 1.50을 출력한다.)

import sys

legend = {"A+":4.3, "A0":4.0, "A-":3.7, "B+":3.3, "B0":3.0, "B-":2.7, "C+":2.3, "C0":2.0, "C-":1.7, "D+":1.3, "D0":1.0, "D-":0.7, "F":0.0}

scores = []

length = int(sys.stdin.readline())

for i in range(length):
    scores.append(sys.stdin.readline().split())

sum = 0.0
total = 0.0
for i in range(length):
    sum += float(scores[i][1]) * legend[scores[i][2]]
    total += float(scores[i][1])

avg = sum/total
avg = round(avg+0.001, 2)
print("%.2f" % avg)