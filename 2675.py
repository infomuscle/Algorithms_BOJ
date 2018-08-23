tc = int(input())

for i in range(0, tc):
    emptyChr = ""
    cs = input().split()
    rptNum = int(cs[0])
    rptChr = cs[1]
    for j in range(0, len(rptChr)):
        emptyChr += (rptNum * rptChr[j])
    print(emptyChr)