import sys

e, s, m = map(int, sys.stdin.readline().split())

year = 0
eTemp, sTemp, mTemp = 0,0,0

while True:
    year += 1
    eTemp += 1
    sTemp += 1
    mTemp += 1
    if eTemp > 15:
        eTemp = 1
    if sTemp > 28:
        sTemp = 1
    if mTemp > 19:
        mTemp = 1
    if eTemp == e and sTemp == s and mTemp == m:
        break

print(year)