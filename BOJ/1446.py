import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]

for i in range(d):
    graph[i].append([i+1, 1])

for _ in range(n):
    start, end, cost = map(int, input().split())
    if end <= d: 
        graph[start].append([end, cost])

distance = [INF] * (d + 1)
distance[0] = 0
queue = []
heapq.heappush(queue, [0, 0])

while queue:
    currentCost, currentNode = heapq.heappop(queue)
    
    if distance[currentNode] < currentCost: continue
    
    for nextNode, nextCost in graph[currentNode]:
        newCost = nextCost + currentCost
        if newCost < distance[nextNode]:
            distance[nextNode] = newCost
            heapq.heappush(queue, [newCost, nextNode])
            
print(distance[-1])