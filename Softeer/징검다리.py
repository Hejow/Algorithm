import sys ; input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))
DP = [1] * n

for i in range(1, n):
    for j in range(i):
        if stones[i] > stones[j]:
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))