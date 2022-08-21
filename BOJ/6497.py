import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    
    parent[y] = x
    
while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0: break
    
    parent = list(range(M))

    graph = []
    for i in range(N):
        start, end, cost = map(int, input().split())
        graph.append([start, end, cost])
    graph.sort(key=lambda x:x[2])

    savedCost = 0
    for edge in graph:
        if find(edge[0]) != find(edge[1]): union(edge[0], edge[1])
        else: savedCost += edge[2]
            
    print(savedCost)