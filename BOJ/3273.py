N = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

start, end = 0, N-1
cnt = 0

while start < end:
    tmp = arr[start] + arr[end]
    if tmp == x: cnt += 1
    if tmp < x:
        start += 1
        continue
    end -= 1
     
print(cnt)