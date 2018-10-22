import sys
import math

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
finds = list(map(int, sys.stdin.readline().split()))

nums.sort()

for i in range(m):
    num = -1
    cnt = 0
    mid = int(len(nums) / 2)
    left, right = 0, len(nums)-1
    while True:
        cnt += 1
        if finds[i] == nums[mid]:
            num = nums[mid]
            break
        elif finds[i] > nums[mid]:
            left = mid+1
            mid = int((left+right)/2)
        else:
            right = mid-1
            mid = int(left+right/2)
        if cnt > math.log(n, 2):
            break

    if num == finds[i]:
        print(1)
    else:
        print(0)