import sys

result = ""

n= int(sys.stdin.readline())

for i in range(n):
    result += str(i+1)

print(len(result))