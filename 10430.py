numIn = input().split(" ")
a, b, c = int(numIn[0]), int(numIn[1]), int(numIn[2])

print((a+b)%c)
print((a%c+b%c)%c)
print((a*b)%c)
print((a%c*b%c)%c)