import sys
input = sys.stdin.readline

MAX = 1000001
ans, case = 0, 1

def check():
    for i in range(N):
        if '.' in board[i]: return False
    return True

def backtracking(x,y,cnt):
    global ans
    if check(): ans = min(ans, cnt)
    if cnt < ans:
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            visitedPoints = []
            nx, ny = x, y
            
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == '.':
                    visitedPoints.append([nx, ny])
                    board[nx][ny] = '*'
                else: break
            
            if visitedPoints: backtracking(nx - dx, ny - dy, cnt + 1)
                
            for a, b in visitedPoints:
                board[a][b] = '.'

while True:
    try:
        N, M = map(int, input().split())
        board = [list(input().strip()) for _ in range(N)]
        ans = MAX
        for i in range(N):
            for j in range(M):
                if board[i][j] == '.':
                    board[i][j] = '*'
                    backtracking(i, j, 0)
                    board[i][j] = '.'
        
        if ans == MAX: ans = -1
        print(f'Case {case}: {ans}')
        case += 1
    except:
        break