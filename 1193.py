# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.

lineLastList = []
lineLast = 1
lineAdder = 2

while lineLast < 11000000:
    lineLastList.append(lineLast)
    lineLast += lineAdder
    lineAdder += 1


order = int(input())

if order == 1:
    print("%d/%d" % (1, 1))

else:
    lineNum = 0
    lineStart = 0

    for i in range(0,len(lineLastList)):
        if order > lineLastList[i]:
            continue
        elif order <= lineLastList[i]:
            lineNum = (i+1)
            lineLast = lineLastList[i]
            lineStart = lineLastList[i-1]+1
            break

    orderInLine = order - lineStart
    a = lineNum - orderInLine
    b = 1 + orderInLine

    if lineNum%2 == 1:
        print("%d/%d" % (a, b))
    elif lineNum%2 == 0:
        print("%d/%d" % (b, a))
