import sys
input = sys.stdin.readline

cnt = 0
n, m = map(int, input().split())
arr = list(map(int, input().split()))
remainder = [0] * m
remainder[0] = 1

total = 0
for i in range(n):
    total += arr[i]
    r = total % m
    # 나머지 값에 따라서 idx 정보 저장
    remainder[r] += 1

for i in remainder:
    cnt += i*(i - 1) // 2

print(cnt)