import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
q, ans = [], []

for i in range(1, N+1):
    if not indegree[i]: q.append(i)
    
while q:
    n = q.pop(0)
    ans.append(n)
    
    for i in graph[n]:
        indegree[i] -= 1
        
        if not indegree[i]: q.append(i)
        
for i in ans:
    print(i, end=' ')