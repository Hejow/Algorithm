import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
DP = [0 for _ in range(k+1)]
DP[0] = 1
for i in coins:
    for j in range(1, k+1):
        if j-i >= 0:
            DP[j] += DP[j-i]
            
print(DP)