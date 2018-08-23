sum = 0
endNum = int(input())

if endNum>=1 and endNum<=10000:
    for i in range(1, endNum+1):
        sum += i

print(sum)