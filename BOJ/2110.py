import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

left, right = 1, home[-1] - home[0]

while left <= right:
    mid = (left + right) // 2
    router = home[0]
    cnt = 1
    
    for i in range(1, n):
        if home[i] >= router + mid:
            router = home[i]
            cnt += 1
            
    if cnt < c: right = mid - 1
    else: 
        left = mid + 1
        ans = mid
    
print(ans)