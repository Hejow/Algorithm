import sys

def BFS(nodes, start):
    queue = [start]
    visisted = [start]
    
    while queue:
        n = queue.pop(0)
        print(n, end=' ')
        
        if n in nodes: 
            tmp = sorted(nodes[n])
            for node in tmp:
                if node not in visisted:
                    queue.append(node)
                    visisted.append(node)
                
def DFS(nodes, start):
    stack = [start]
    visited = []
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in nodes: stack += sorted(nodes[n], reverse=True)
    
    for v in visited:
        print(v, end=' ')
        
N, M, V = map(int, sys.stdin.readline().split())
nodes = {}
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    nodes[x] = nodes.get(x, []) + [y]
    nodes[y] = nodes.get(y, []) + [x]
    
DFS(nodes, V)
print()
BFS(nodes, V)