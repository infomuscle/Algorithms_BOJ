scale = input().split()
checker = 0

for i in range(0,len(scale)):
    scale[i] = int(scale[i])

for i in range(0,len(scale)-1):
    if scale[i] < scale[i+1]:
        checker += 1

if checker == 7:
    print("ascending")
elif checker == 0:
    print("descending")
else:
    print("mixed")