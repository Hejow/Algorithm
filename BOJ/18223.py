import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

V, E, P = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])
    graph[end].append([cost, start])

def dijkstra(start):
    distances = [INF] * (V+1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    
    while q:
        currentCost, currentNode = heapq.heappop(q)
        
        if distances[currentNode] < currentCost: continue
        
        for nextCost, nextNode in graph[currentNode]:
            newCost = nextCost + currentCost
            if newCost < distances[nextNode]:
                distances[nextNode] = newCost
                heapq.heappush(q, [newCost, nextNode])
    
    return distances

print("SAVE HIM" if dijkstra(1)[V] == (dijkstra(1)[P] + dijkstra(P)[V]) else "GOOD BYE")