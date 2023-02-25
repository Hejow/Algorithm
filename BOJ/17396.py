import heapq, sys
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        currentCost, currentNode = heapq.heappop(q)
        
        if distance[currentNode] < currentCost: continue
        
        for nextCost, nextNode in graph[currentNode]:
            newCost = currentCost + nextNode
            if newCost < distance[nextCost] and wards[nextCost] == 0:
                distance[nextCost] = newCost
                heapq.heappush(q, (newCost, nextCost))

N, M = map(int, input().split())
distance = [INF]*(N+1)
wards = list(map(int, input().split()))
wards[-1] = 0

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))
dijkstra(0)
print(distance[N-1] if distance[N-1] != INF else -1)