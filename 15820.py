import sys

s1, s2 = map(int, sys.stdin.readline().split())

sampleFlag = 1
for i in range(s1):
    answer, submit = map(int,sys.stdin.readline().split())
    if answer != submit:
        sampleFlag = 0
        break

systemFlag = 1
for i in range(s2):
    answer, submit = map(int, sys.stdin.readline().split())
    if answer != submit:
        systemFlag = 0
        break

if sampleFlag == 1 and systemFlag == 1:
    print("Accepted")
elif sampleFlag == 0:
    print("Wrong Answer")
elif systemFlag == 0:
    print("Why Wrong!!!")