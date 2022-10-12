import heapq, sys
input = sys.stdin.readline

n = int(input())
dict = {}

for i in range(n):
    v, w = map(int, input().split())
    if v not in dict:
        dict[v] = [[-w, -(i+1)]]
    else:
        heapq.heappush(dict[v], [-w, -(i+1)])

tmp, ans = [], 0

for k in dict.keys():
    if k in tmp: continue
    ans += -(heapq.heappop(dict[k])[1])
    
print(ans)