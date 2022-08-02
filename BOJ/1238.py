import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(1, M+1):
    s, e, c = map(int, input().split())
    graph[s].append([c,e])

to_dest, from_dest = [INF] * (N+1), [INF] * (N+1)
max_ = 0
queue = []

def dijkstra(start, dist):
    dist[start] = 0
    heapq.heappush(queue, [0, start])
    
    while queue:
        current_cost, current_node = heapq.heappop(queue)
        
        if dist[current_node] < current_cost: continue
        
        for new_cost, new_node in graph[current_node]:
            distance = new_cost + current_cost
            if distance < dist[new_node]:
                dist[new_node] = distance
                heapq.heappush(queue, [distance, new_node])
           
dijkstra(X, from_dest)
for i in range(1, N+1):
    dijkstra(i, to_dest)
    max_ = max(max_ ,to_dest[X] + from_dest[i])
    to_dest = [INF] * (N+1)
    
print(max_)