import sys

n = int(sys.stdin.readline())
nums = []

for i in range(0, n):
    num = int(sys.stdin.readline())
    nums.append(num)

nums.sort()

for i in range(0, n):
    print(nums[i])