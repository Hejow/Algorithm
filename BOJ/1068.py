import sys

def DFS(t):
    stack = [t]
    cnt = 0
    
    while stack:
        n = stack.pop()
        if n in d:
            stack.extend(d[n])
            del d[n]
            
    for k in d:
        if t in d[k]:
            d[k].remove(t)
            
    for k in d:
        if not d[k] and k != -1: 
            cnt += 1
    
    print(cnt)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())
d = {}

for i, v in enumerate(arr):
    if i not in d: d[i] = []
    d[v] = d.get(v, []) + [i]
    
DFS(t)