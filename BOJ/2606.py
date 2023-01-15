import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = list([] for _ in range(n+1))
cnt = 0

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    
queue, check = list(), set([1])
queue.extend(graph[1])

while queue:
    next = queue.pop()
    
    if next not in check:
        check.add(next)
        queue.extend(graph[next])
        cnt += 1

print(cnt)