import sys

n, k = map(int, sys.stdin.readline().split())
mod = 1000000000
DP = [0 for _ in range(n+1)]
DP[0] = 1

for _ in range(1, k+1):
    for i in range(1, n+1):
        DP[i] = (DP[i] + DP[i-1]) % mod
        
print(DP[n])