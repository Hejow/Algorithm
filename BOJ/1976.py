import sys
input = sys.stdin.readline

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]

def union(x, y):
    x = find(x)
    y = find(y)
    
    parent[y] = x
    
N = int(input())
M = int(input())
parent = list(range(N+1))
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j]: union(i, j+1)

plans = list(map(int, input().split()))
ans = set([find(p) for p in plans])

if len(ans) == 1: print('YES')
else: print('NO')