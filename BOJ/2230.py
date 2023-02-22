import sys
input = sys.stdin.readline

def solution(n, m, arr):
    start, end = 0, 1
    min_ = sys.maxsize
    
    while start < n and end < n:
        calc = arr[end] - arr[start]
        if calc == m: return m
        if calc < m:
            end += 1
            continue
        start += 1
        min_ = min(min_, calc)
        
    return min_

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input().rstrip()))

arr.sort()
print(solution(n, m, arr))