import sys

def AatB(a, b):
    result = (a+b)*(a-b)
    return result

a, b = map(int, sys.stdin.readline().split())
print(AatB(a,b))