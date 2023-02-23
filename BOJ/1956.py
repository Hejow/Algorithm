import sys
input = sys.stdin.readline

INF = int(1e9)

def initBoard():
    board = [[INF] * (v+1) for _ in range(v+1)]
    
    for i in range(1, v+1):
        board[i][i] = 0
    
    for _ in range(e):
        start, end, cost = map(int, input().split())
        board[start][end] = cost
    
    return board

def floydWarshall(board):
    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])
                
def findCourse(start, board):
    sumCourse = INF
    
    for i in range(v+1):
        if start == i: continue
        sumCourse = min(sumCourse, board[start][i] + board[i][start])
        
    return sumCourse

v, e = map(int, input().split())
board = initBoard()
floydWarshall(board)

course = INF
for i in range(1, v+1):
    course = min(course, findCourse(i, board))
    
print(course if course != INF else -1)