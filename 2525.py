nowTime = input().split(" ")
cTime = int(input())

hour = int(nowTime[0])
minute = int(nowTime[1])

minute += cTime
hour += int(minute/60)
minute = minute%60

if hour >= 24:
    hour -= 24

print("%d %d" % (hour, minute))