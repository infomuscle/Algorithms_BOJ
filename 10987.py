# 문제
# 알파벳 소문자로만 이루어진 단어가 주어진다.
# 이때, 모음(a, e, i, o, u)의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어가 주어진다.
# 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 첫째 줄에 모음의 개수를 출력한다.

import sys

word = sys.stdin.readline().rstrip()
cnt = 0

for i in range(len(word)):
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
        cnt += 1

print(cnt)