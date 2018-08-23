c = int(input())
rtime = 0
while True:
    tc = input().split()
    for i in range(0, len(tc)):
        tc[i] = int(tc[i])
    total = 0
    for j in range(1, len(tc)):
        total += tc[j]
    avg = total/(len(tc)-1)
    avgUp = []
    for k in range(1, len(tc)):
        if tc[k] > avg:
            avgUp.append(tc[k])
    ratio = len(avgUp)/(len(tc)-1)
    percent = ratio * 100
    print("%.3f%%" % percent)

    rtime += 1
    if rtime >= c:
        break