# 문제
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다.
# 따라서, 다음과 같이 크로아티아 알파벳을 다음과 같이 변경해서 입력했다.
# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# ñ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다.
# lj와 nj도 마찬가지이다.
# 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다.
# 알파벳 소문자와 '-', '='로만 이루어져 있다.
# 문제 설명에 나와있는 크로아티아 알파벳만 주어진다.

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

cAlpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

inStr = input()

for i in range(len(inStr)):
    count += 1
    if i == len(inStr) - 1:
        break

    if inStr[i] == "c" and inStr[i+1] == "=":
        count -= 1
    elif inStr[i] == "c" and inStr[i+1] == "-":
        count -= 1
    elif inStr[i] == "d" and inStr[i+1] == "z" and inStr[i+2] == "=":
        count -= 1
    elif inStr[i] == "d" and inStr[i+1] == "-":
        count -= 1
    elif inStr[i] == "l" and inStr[i+1] == "j":
        count -= 1
    elif inStr[i] == "n" and inStr[i+1] == "j":
        count -= 1
    elif inStr[i] == "s" and inStr[i+1] == "=":
        count -= 1
    elif inStr[i] == "z" and inStr[i+1] == "=":
        count -= 1

print(count)