from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque([])
moves = [(-1,0), (1,0), (0,-1), (0,1)]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = moves[i] + x, moves[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

BFS()
for i in matrix:
    if 0 in matrix[i]:
        print(-1)
        sys.exit(0)
    res = max(res, max(i))
print(res - 1)