import sys, copy

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_ = 0

def move(board, m):
    if m == 'U': # 위
        for y in range(n):
            end = 0
            for x in range(1, n):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[end][y] == 0:
                        board[end][y] = tmp
                    elif board[end][y] == tmp:
                        board[end][y] *= 2
                        end += 1
                    else:
                        end += 1
                        board[end][y] = tmp
    if m == 'D': # 아래
        for y in range(n):
            end = n-1
            for x in range(n-2, -1, -1):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[end][y] == 0:
                        board[end][y] = tmp
                    elif board[end][y] == tmp:
                        board[end][y] *= 2
                        end -= 1
                    else:
                        end -= 1
                        board[end][y] = tmp
    if m == 'L': # 왼쪽
        for x in range(n):
            end = 0
            for y in range(1, n):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[x][end] == 0:
                        board[x][end] = tmp
                    elif board[x][end] == tmp:
                        board[x][end] *= 2
                        end += 1
                    else:
                        end += 1
                        board[x][end] = tmp
                        
    if m == 'R': # 오른쪽
        for x in range(n):
            end = n-1
            for y in range(n-2, -1, -1):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[x][end] == 0:
                        board[x][end] = tmp
                    elif board[x][end] == tmp:
                        board[x][end] *= 2
                        end -= 1
                    else:
                        end -= 1
                        board[x][end] = tmp
        
    return board

def backtracking(board, cnt):
    global max_
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                max_ = max(max_, board[i][j])
        return
    
    for m in 'UDLR':
        tmp = move(copy.deepcopy(board), m)
        backtracking(tmp, cnt+1)
        
backtracking(board, 0)
print(max_)