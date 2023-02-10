import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

copied = [b[:] for b in board]
for i in range(n):
    for j in range(1, n):
        copied[i][j] += copied[i][j-1] 
        
def calculate(x1, y1, x2, y2):
    sum = 0
    
    if x1 == x2 and y1 == y2:
        print(board[x1][y1])
        return
    
    for i in range(x1, x2 + 1):
        if y1 == 0: sum += copied[i][y2]
        else: sum += (copied[i][y2] - copied[i][y1-1])
    
    print(sum)
    return 

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    calculate(x1-1, y1-1, x2-1, y2-1)