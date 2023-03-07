import sys ; input = sys.stdin.readline
from collections import Counter

row, column = 3, 3

def rFun(board):
    for r in range(row):
        s = sorted(Counter(board[r]).most_common(), key=lambda x:(x[1], x[0]))
        tmp = []
        for e in s:
            tmp.extend(e)
        
        
def cFun(board):
    for j in range(column):
        for i in range(row):
            return 0
    
    return 0

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

for i in range(100):
    if row >= column: rFun(board)
    else: cFun(board)
    
    if board[r][c] == k:
        print(i)
        sys.exit()

print(-1)