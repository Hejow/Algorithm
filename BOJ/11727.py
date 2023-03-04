import sys ; input = sys.stdin.readline

MOD = 10007

def calc(n):
    DP = [0] * 1001
    DP[1], DP[2] = 1, 3
    
    for i in range(3, n+1):
        DP[i] = DP[i-1] + 2 * DP[i-2]
    
    return DP[n] % MOD

n = int(input())
print(calc(n))