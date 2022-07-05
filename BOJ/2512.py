import sys

N = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
budget.sort()

def binary(budget):
    left, right = 0, max(budget)
    while left <= right:
        mid, sum_ = (left + right) // 2, 0
        for num in budget: 
            sum_ += min(mid, num)
        if sum_ > M: right = mid - 1
        else: left = mid + 1
        
    return right

print(binary(budget))