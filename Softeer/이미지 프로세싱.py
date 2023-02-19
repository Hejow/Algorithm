import sys
input = sys.stdin.readline

moves = [(1,0), (0,1), (-1,0), (0,-1)]

h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
q = int(input())

for _ in range(q):
    i, j, c = map(int, input().split())

    if board[i-1][j-1] == c:
        continue

    target = board[i-1][j-1]
    q = [[i-1, j-1]]

    while q:
        x, y = q.pop(0)

        if 0 <= x < h and 0 <= y < w and board[x][y] == target:
            board[x][y] = c
            
            for i in range(4):
                q += [x + moves[i][0], y + moves[i][1]],

for row in board:
    print(' '.join(map(str, row)))