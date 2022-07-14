import sys

N = int(sys.stdin.readline())
board = [sys.stdin.readline().strip() for _ in range(N)]
nboard = [[] for _ in range(N)]

for i in range(N):
    nboard[i] = board[i].replace('G','R')

moves = [(-1,0), (1,0), (0,-1), (0,1)]
visited = [[False] * N for _ in range(N)]

def BFS(x, y, bd):
    queue = [[x,y]]
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx, ny = x + moves[i][0], y + moves[i][1]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and bd[x][y] == bd[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                
cnt = 0
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            BFS(x, y, board)
            cnt += 1
print(cnt, end=' ')

cnt = 0
visited = [[False] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            BFS(x, y, nboard)
            cnt += 1
print(cnt)