import sys, heapq
input = sys.stdin.readline

MOD = 1000000007

for _ in range(int(input())):
    N = int(input())
    energy = list(map(int, input().split()))
    heapq.heapify(energy)
    cost = 1
    
    while len(energy) > 1:
        tmp = heapq.heappop(energy) * heapq.heappop(energy)
        cost *= tmp
        heapq.heappush(energy, tmp)
            
    print(cost % MOD)