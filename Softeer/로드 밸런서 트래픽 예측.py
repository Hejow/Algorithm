import sys, collections
input = sys.stdin.readline

n, k = map(int, input().split())

balancer = collections.defaultdict(list)
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    if len(tmp) > 1: balancer[i] = tmp[1:]

def getOrder(n):
    indegree = [0] * (n+1)
    
    for k, nodes in balancer.items():
        for n in nodes:
            indegree[n] += 1
            
    q = [1]
    order = []
    
    while q:
        i = q.pop(0)
        order += i,
        
        for node in balancer[i]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q += node,
                
    return order

def runServer(order):
    requests = collections.defaultdict(int)
    requests[1] = k
    
    for node in order:
        nextNodes = len(balancer[node])
        if nextNodes == 0: continue
        
        totalRequest = requests[node]
        for i, nextNode in enumerate(balancer[node], start= 1):
            nextRequest = totalRequest // nextNodes
            
            if i <= totalRequest % nextNodes:
                nextRequest += 1
                
            requests[nextNode] += nextRequest
    
    return requests
        
order = getOrder(n)
requests = runServer(order)

requests = sorted(requests.items(), key=lambda x:x[0])
requests = [v for k, v in requests]
print(' '.join(map(str, requests)))