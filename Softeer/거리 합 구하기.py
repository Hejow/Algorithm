import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(graph, start, size):
    distance = [INF] * (size+1)
    distance[start] = 0
    queue = []
    
    heapq.heappush(queue, [0, start])
    
    while queue:
        currentCost, currentNode = heapq.heappop(queue)
        
        if distance[currentNode] < currentCost: continue
        
        for nextCost, nextNode in graph[currentNode]:
            newCost = nextCost + currentCost
            if newCost < distance[nextNode]:
                distance[nextNode] = newCost
                heapq.heappush(queue, [newCost, nextNode])
    
    sum_ = 0
    for cost in distance:
        if cost == INF: continue
        sum_ += cost
        
    return sum_

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])
    graph[end].append([cost, start])
    
for i in range(1, n+1):
    print(dijkstra(graph, i, n))