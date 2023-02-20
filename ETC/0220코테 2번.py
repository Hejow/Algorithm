parent = [i for i in range(100000)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    parent[y] = x

def solution(paths):
    paths = sorted(paths)
    starts = []
    answer = []
    
    for path in paths:
        start, end = path
        if start > end:
            starts.append([end, True])
            union(start, end)
        else:
            starts.append([start, False])
            union(end, start)
            
    for start, isReversed in sorted(starts):
        end = find(start)
        if end not in answer:
            if isReversed:
                answer.append(end)
                answer.append(start)
            else:
                answer.append(start)
                answer.append(end)
    
    return answer

paths = [[1,2],[2,3],[3,4],[8,7],[7,6]]
print(solution(paths))