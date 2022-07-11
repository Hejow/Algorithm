import sys
input = sys.stdin.readline

def check(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            print('no')
            return
    print('yes')

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [str(input().strip()) for _ in range(n)]
    nums.sort()
    
    check(nums)