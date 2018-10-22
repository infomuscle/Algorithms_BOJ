# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다.
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1≤M≤100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수들의 범위는 int 로 한다.

# 출력
# M개의 줄에 답을 출력한다.
# 존재하면 1을, 존재하지 않으면 0을 출력한다.

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
finds = list(map(int, sys.stdin.readline().split()))

nums.sort()

for i in range(m):
    num = None
    left, right = 0, len(nums)-1
    mid = int(left+right/2)
    while left<=right:
        mid = int((left + right) / 2)
        if finds[i] == nums[mid]:
            num = nums[mid]
            break
        elif finds[i] > nums[mid]:
            left = mid+1
        else:
            right = mid-1

    if num == finds[i]:
        print(1)
    else:
        print(0)