import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges= []
for _ in range(E):
    edges.append(list(map(int, input().split())))    
edges.sort(key=lambda x:x[2])

parent = list(range(V+1))

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    
    parent[y] = x

cnt, ans = 0, 0
while True:
    if cnt == V-1: break
    edge = edges.pop(0) # start, end, cost
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        ans += edge[2]
        cnt += 1
    
print(ans)