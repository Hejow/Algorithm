import sys ; input = sys.stdin.readline
UP, DOWN, LEFT, RIGHT = 3, 4, 2, 1
direction = {
    DOWN: (1,0),
    UP: (-1,0),
    LEFT: (0,-1),
    RIGHT: (0,1)
}

def turnDice(move):
    global dice
    if move == UP:
        tmp = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = tmp
    elif move == DOWN:
        tmp = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = dice[1]
        dice[1] = tmp
    elif move == LEFT:
        tmp = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = tmp
    else:
        tmp = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = tmp

def changeDice(board):
    global dice
    if board[nx][ny] == 0:
        board[nx][ny] = dice[6]
    else:
        dice[6] = board[nx][ny]
        board[nx][ny] = 0

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
dice = {i : 0 for i in range(1,7)}

for move in moves:
    nx = x + direction[move][0]
    ny = y + direction[move][1]
    
    if 0 > nx or n <= nx or 0 > ny or m <= ny: continue
    turnDice(move)
    changeDice(board)
    x = nx ; y = ny
    
    print(dice[1])