import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1,N+1):
    c = combinations(arr, i)
    
    for n in c:
        if sum(n) == M: cnt+=1

print(cnt)