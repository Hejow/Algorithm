import sys ; input = sys.stdin.readline

N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]
DP =[[0] * N for _ in range(N)] 

for i in range(1, N):
    for j in range(N-i):
    
        if i == 1:
            DP[j][j+i] = p[j][0] * p[j][1] * p[j+i][1]
            continue
        
        DP[j][j+i] = 2**32
        for k in range(j, j+i): 
            DP[j][j+i] = min(DP[j][j+i], DP[j][k] + DP[k+1][j+i] + p[j][0] * p[k][1] * p[j+i][1])
    
print(DP[0][N-1])