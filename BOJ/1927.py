import heapq, sys

input = sys.stdin.readline
n = int(input())
q = []

for _ in range(n):
    tmp = int(input())
    if not tmp:
        if not q: print(0)
        else: print(heapq.heappop(q))
    else:
        heapq.heappush(q, tmp)