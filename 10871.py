nx = input().split(" ")
for i in range(0, len(nx)):
    nx[i] = int(nx[i])

a = input().split(" ")
for i in range(0, len(a)):
    a[i] = int(a[i])

for i in a:
    if i < nx[1]:
        print(i)
