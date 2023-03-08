import sys ; input = sys.stdin.readline
from collections import Counter

def rFun():
    maxSize = 0
    for r in range(len(board)):
        s = sorted(Counter(board[r]).most_common(), key=lambda x:(x[1], x[0]))
        tmp = []
        for num, cnt in s:
            if num == 0: continue
            tmp.append(num)
            tmp.append(cnt)
        board[r] = tmp
        maxSize = max(maxSize, len(tmp))
    
    for r in range(len(board)):
        board[r] += [0 for _ in range(maxSize - len(board[r]))]
        board[r] = board[r][:100]

def cFun():
    global board
    board = list(zip(*board))
    rFun()
    board = list(zip(*board))

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

for i in range(101):
    try:
        if board[r-1][c-1] == k:
            print(i)
            break
    except: pass
    if len(board) >= len(board[0]): rFun()
    else: cFun()
else: print(-1)