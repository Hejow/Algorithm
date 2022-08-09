N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum_ = arr[0]
ans = 100001

while end < N:
    if sum_ < S:
        end += 1
        sum_ += arr[end]
    else:
        if sum_ == S: ans = min(ans, end - start + 1)
        sum_ -= arr[start]
        start += 1
        
print(ans if ans != 100001 else 0)