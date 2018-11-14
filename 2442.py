import sys

n = int(sys.stdin.readline())
leng = 2*n-1

for i in range(n):
    star = "*"
    cnt = 2*(i+1)-1
    print((star*cnt).center(leng," "))
