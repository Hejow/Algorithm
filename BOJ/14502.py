import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

moves = [(1,0), (0,1), (-1,0), (0,-1)]
MAX_WALL = 3

def countSafeZone(board):
    global safeZone
    cnt = 0
    
    for b in board:
        cnt += b.count(0)
    
    safeZone = max(safeZone, cnt)

def bfs(board):
    q = deque(givenVirus)
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + moves[i][0]
            ny = y + moves[i][1]
            
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append([nx, ny])
                
    countSafeZone(board)

def arrangeWall(cnt):
    if cnt == MAX_WALL:
        bfs(deepcopy(board))
        return
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                arrangeWall(cnt + 1)
                board[i][j] = 0

safeZone = 0
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

givenVirus = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            givenVirus.append([i, j])

arrangeWall(0)
print(safeZone)