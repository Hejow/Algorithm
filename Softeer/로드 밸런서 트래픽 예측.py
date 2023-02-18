import sys
input = sys.stdin.readline

n, k = map(int, input().split())
requests = [0] * (n + 1)

balancer = {}
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    
    if len(tmp) > 1: 
        balancer[i] = tmp[1:]


print(' '.join(map(str, requests[1:])))