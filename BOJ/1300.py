import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

left, right = 1, k

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    
    for i in range(1, n+1):
        cnt += min(mid//i, n)
        
    if cnt >= k:
        ans = mid
        right = mid - 1
    else: 
        left = mid + 1
    
print(ans)