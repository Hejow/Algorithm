import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
points = []
for _ in range(N):
    points.append(list(map(int, input().split())))

edges = []
for i in range(N):
    for j in range(i+1, N):
        dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2) ** 0.5
        heapq.heappush(edges, [dist, i+1, j+1])

parent = list(range(N+1))

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    parent[y] = x
    
cnt, ans = 0, 0

for _ in range(M):
    x, y = map(int, input().split())
    if find(x) != find(y):
        union(x, y)
        cnt += 1

while True:
    if cnt == N-1: break
    
    edge = heapq.heappop(edges)
    
    if find(edge[1]) != find(edge[2]):
        union(edge[1], edge[2])
        ans += edge[0]
        cnt += 1
        
print(f'{ans:.2f}')