import sys
from collections import deque
input = sys.stdin.readline
INF = int(10e9)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

dist = [INF] * (N+1)
dist[X] = 0
q = deque([X])

while q:
    node = q.popleft()
    
    for n in graph[node]:
        if dist[n] == INF:
            dist[n] = min(dist[n], dist[node] + 1)
            q.append(n)
        
if K not in dist:
    print(-1)
    exit(0)

for i in range(1, N+1):
    if dist[i] == K:
        print(i)