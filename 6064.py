import sys

def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

def lcm(a, b):
  gcd_value = gcd(a, b)
  if (gcd_value == 0): return 0
  return abs( (a * b) / gcd_value )

tc = int(sys.stdin.readline())

for t in range(tc):
    m,n,x,y = map(int, sys.stdin.readline().split())

    a, b, cnt = 0,0,0

    while 1:
        a +=1
        if a>m:
            a = 1
        b += 1
        if b>n:
            b = 1
        cnt += 1
        if (a == x and b == y) or cnt > lcm(m,n):
            break

    if cnt>lcm(m,n):
        print(-1)
    else:
        print(cnt)
# m = 10, n = 12, x = 3, y = 2
# 1 - 1:1       21 - 1:9     41 - 1:5
# 2 - 2:2       22 - 2:10    42 - 2:6
# 3 - 3:3       23 - 3:11    43 - 3:7
# 4 - 4:4       24 - 4:12    44 - 4:8
# 5 - 5:5       25 - 5:1     45 - 5:9
# 6 - 6:6       26 - 6:2     46 - 6:10
# 7 - 7:7       27 - 7:3     47 - 7:11
# 8 - 8:8       28 - 8:4     48 - 8:12
# 9 - 9:9       29 - 9:5     49 - 9:1
# 10 - 10:10    30 - 10:6    50 - 10:2
# 11 - 1:11     31 - 1:7     51 - 1:3
# 12 - 2:12     32 - 2:8     52 - 2:4
# 13 - 3:1      33 - 3:9     53 - 3:5
# 14 - 4:2      34 - 4:10    54 - 4:6
# 15 - 5:3      35 - 5:11    55 - 5:7
# 16 - 6:4      36 - 6:12    56 - 6:8
# 17 - 7:5      37 - 7:1     57 - 7:9
# 18 - 8:6      38 - 8:2     58 - 8:10
# 19 - 9:7      39 - 9:3     59 - 9:11
# 20 - 10:8     40 - 10:4    60 - 10:12