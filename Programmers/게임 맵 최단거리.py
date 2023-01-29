moves = [(1,0), (0,1), (-1,0), (0,-1)]

def solution(maps):
    row = len(maps)
    column = len(maps[0])
    
    graph = [[-1 for _ in range(column)] for _ in range(row)]
    graph[0][0] = 1
    
    queue = []
    queue.append([0, 0])
    
    while queue:
        y, x = queue.pop(0)
        
        for i in range(4):
            nx = x + moves[i][0]
            ny = y + moves[i][1]
            
            if 0 <= nx < column and 0 <= ny < row and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])
                
    return graph[-1][-1]