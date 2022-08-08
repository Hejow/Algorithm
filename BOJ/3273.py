N = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

cnt, end = 0, N-1

for start in range(N):
    while start < end:
        tmp = arr[start] + arr[end]
        if tmp > x: end -=1
        elif tmp < x: start += 1
        else: 
            cnt += 1
            break
        
print(cnt)