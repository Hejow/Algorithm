import sys, heapq

N, K = map(int, sys.stdin.readline().split())
J = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
C = [int(sys.stdin.readline()) for _ in range(K)]
J.sort()
C.sort()

sum_ = 0
tmp = []

for capacity in C:
    while J and J[0][0] <= capacity:
        heapq.heappush(tmp, -heapq.heappop(J)[1])
        
    if tmp: sum_ += -heapq.heappop(tmp)
    elif not J: break
    
print(sum_)