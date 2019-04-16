# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다.
# 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
# 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만,
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때,
# 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

weight = int(input())

# 10, 15, 20, 25, ... 3 = 0, 5 = 2,3,4,5,6,7
list0 = []

# 8, 13, 18, 23, ... 3 = 1, 5 = 1,2,3,4,5,6
list1 = []

# 11, 16, 21, 26, ... 3 = 2, 5 = 1,2,3,4,5,6
list2 = []

# 9, 14, 19, 24, ... 3 = 3, 5 = 0,1,2,3,4,5
list3 = []

# 12, 17, 22, 27, ... 3 = 4, 5 = 0,1,2,3,4,5
list4 = []

for i in range(2, 1001):
    a = i*5
    list0.append(a)

for i in range(1, 1000):
    b = 3*1 + i*5
    list1.append(b)

for i in range(1, 999):
    c = 3*2 + i*5
    list2.append(c)

for i in range(0, 999):
    d = 3*3 + i*5
    list3.append(d)

for i in range(0, 998):
    e = 3*4 + i*5
    list4.append(e)

if weight == 3 or weight == 5:
    print(1)
elif weight == 6:
    print(2)
elif weight == 4 or weight == 7:
    print(-1)
else:
    if weight in list0:
        aa = list0.index(weight)
        print(aa+2)
    elif weight in list1:
        bb = list1.index(weight)
        print(bb+1+1)
    elif weight in list2:
        cc = list2.index(weight)
        print(cc+1+2)
    elif weight in list3:
        dd = list3.index(weight)
        print(dd+3)
    elif weight in list4:
        ee = list4.index(weight)
        print(ee+4)
    else:
        print("ERROR")