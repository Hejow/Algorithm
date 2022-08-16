import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수(vertex), 버스의 개수(edge) 입력
N = int(input())
M = int(input())

# 입력 받은 값 그래프화
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    # heapq를 사용하기 때문에 비용을 먼저 저장
    graph[start].append((cost, end))

# 출발점, 도착점 입력
start, end = map(int, input().split())
    
# 다익스트라 함수
def dijkstra(start):
    # 최단거리 계산용 리스트
    dist = [INF] * (N+1)
    dist[start] = 0
    q = []
    # 방문하지 않은 노드 중에서 가장 cost가 적은 노드를 선택하야 함으로 heapq를 사용
    heapq.heappush(q, [0, start])
    
    while q:
        current_cost, current_node = heapq.heappop(q)
        
        # 기존에 있는 비용보다 더 비용이 크다면 따질 필요가 없다.
        if dist[current_node] < current_cost: continue
        
        for next_cost, next_node in graph[current_node]:
            new_cost = current_cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(q, [new_cost, next_node])
                
    return dist
                
print(dijkstra(start)[end])