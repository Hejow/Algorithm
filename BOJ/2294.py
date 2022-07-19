import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
DP = [100001 for _ in range(k+1)]
DP[0] = 0

for c in coins:
    for i in range(1, k+1):
        if i-c>=0:
            DP[i] = min(DP[i], DP[i-c] + 1)

print(-1) if DP[k] == 100001 else print(DP[k])