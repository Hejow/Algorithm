import sys ; input = sys.stdin.readline
from collections import deque

def solution(w, graph, inDegree, d):
    size = len(graph)
    DP = [0] * size
    q = deque()
    
    for i in range(1, size):
        if inDegree[i] == 0:
            q.append(i)
            DP[i] = d[i]
    
    while q:
        v = q.popleft()
        
        for n in graph[v]:
            inDegree[n] -= 1
            DP[n] = max(DP[n], DP[v] + d[n])
            if inDegree[n] == 0:
                q.append(n)
    
    return DP[w]

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    inDegree = [0] * (n+1)
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1
    
    w = int(input())
    print(solution(w, graph, inDegree, d))