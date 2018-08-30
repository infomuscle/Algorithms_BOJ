def summer(k, n):
    sum = 0
    if k == 1:
        for i in range(1, n+1):
            sum += i
        return sum
    else:
        for i in range(1, n+1):
            sum += summer(k-1, i)
        return sum

tc = int(input())

for i in range(tc):
    k = int(input())
    n = int(input())
    print(summer(k,n))