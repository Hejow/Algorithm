import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input().strip())

wx, wy = (0, 0)
flag = False

for x in range(R):
    if flag : break
    for y in range(C):
        if board[x][y] != '.' and board[x][y] != 'M' and board[x][y] != 'Z':
            if board[x][y] == '|':
                for nx in [x-1, x+1]:
                    if board[nx][y] == '.': 
                        wx, wy = (nx,y)
                        flag = True
            if board[x][y] == '-':
                for ny in [y-1, y+1]:
                    if board[x][ny] == '.': 
                        wx, wy = (x, ny)
                        flag = True
            if board[x][y] == '1':
                for nx, ny in [(x+1, y), (x, y+1)]:
                    if board[nx][ny] == '.': 
                        wx, wy = (nx, ny)
                        flag = True
            if board[x][y] == '2':
                for nx, ny in [(x-1, y), (x, y+1)]:
                    if board[nx][ny] == '.': 
                        wx, wy = (nx, ny)
                        flag = True
            if board[x][y] == '3':
                for nx, ny in [(x, y-1), (x-1, y)]:
                    if board[nx][ny] == '.': 
                        wx, wy = (nx, ny)
                        flag = True
            if board[x][y] == '4':
                for nx, ny in [(x+1, y), (x, y-1)]:
                    if board[nx][ny] == '.': 
                        wx, wy = (nx, ny)
                        flag = True
            if board[x][y] == '+':
                for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if board[nx][ny] == '.': 
                        wx, wy = (nx, ny)
                        flag = True

# 위쪽, 왼쪽, 오른쪽, 아래쪽 순서
pipe = [False] * 4

if wx-1 >= 0: pipe[0] = board[wx-1][wy]
if wy-1 >= 0: pipe[1] = board[wx][wy-1]
if wy+1 < C: pipe[2] = board[wx][wy+1]
if wx+1 < R: pipe[3] = board[wx+1][wy]

if pipe[0] in ['-', '2', '3', '.', 'M', 'Z']: pipe[0] = False
if pipe[1] in ['|', '3', '4', '.', 'M', 'Z']: pipe[1] = False
if pipe[2] in ['|', '1', '2', '.', 'M', 'Z']: pipe[2] = False
if pipe[3] in ['-', '1', '4', '.', 'M', 'Z']: pipe[3] = False

if pipe[0] and pipe[1] and pipe[2] and pipe[3]: print(wx+1, wy+1, '+')
elif pipe[0] and pipe[3]: print(wx+1, wy+1, '|')
elif pipe[1] and pipe[2]: print(wx+1, wy+1, '-')
elif pipe[2] and pipe[3]: print(wx+1, wy+1, 1)
elif pipe[0] and pipe[2]: print(wx+1, wy+1, 2)
elif pipe[0] and pipe[1]: print(wx+1, wy+1, 3)
elif pipe[1] and pipe[3]: print(wx+1, wy+1, 4)