days = ["SUN","MON","TUE","WED","THU","FRI","SAT",]
month31 = [1,3,5,7,8,10,12]
month30 = [4,6,9,11]
month2 = [2]
dateChoice = input().split(" ")
month = int(dateChoice[0])
date = int(dateChoice[1])
howLong = 0

for i in range(0, month):
    if i in month31:
        howLong += 31
    elif i in month30:
        howLong += 30
    elif i in month2:
        howLong += 28
    else:
        pass

howLong += date

print(days[howLong%7])