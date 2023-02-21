import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs1(current, parent, subtree_size, dist_sum):
    subtree_size[current] = 1
    for i in range(len(graph[current])):
        child = graph[current][i][0]
        weight = graph[current][i][1]
        
        if child != parent:
            dfs1(child, current, subtree_size, dist_sum)
            subtree_size[current] += subtree_size[child]
            dist_sum[current] += dist_sum[child] + weight * subtree_size[child]
            
    return subtree_size,dist_sum

def dfs2(current, parent, subtree_size, dist_sum):
    for i in range(len(graph[current])):
        child = graph[current][i][0]
        weight = graph[current][i][1]
        
        if child != parent:
            dist_sum[child] = dist_sum[current] + weight * (n - subtree_size[child]) - weight * subtree_size[child]
            dfs2(child, current, subtree_size, dist_sum)
            
    return dist_sum

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x,y,t = map(int,input().split())
    graph[x].append((y,t))
    graph[y].append((x,t))
    
subtree_size, dist_sum = dfs1(1, 1, [0]*(n+1), [0]*(n+1))
dist_sum = dfs2(1, 1, subtree_size, dist_sum)

for i in range(1,n+1):
    print(dist_sum[i])