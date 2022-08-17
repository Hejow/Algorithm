import sys
input = sys.stdin.readline

N, K = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]    
for _ in range(K):
    start, end = map(int, input().split())
    graph[start][end] = 1
    
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

S = int(input())
for _ in range(S):
    x, y = map(int, input().split())
    if graph[x][y]: print(-1)
    elif graph[y][x]: print(1)
    else: print(0)