import sys ; input = sys.stdin.readline
from collections import deque

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
SIZE = 5

def initBoard(key):
    board = [[0] * SIZE for _ in range(SIZE)]
    tmp = ""

    for ch in key:
        if ch not in tmp:
            tmp += ch

    for ch in ALPHABET:
        if ch not in tmp:
            tmp += ch

    for i in range(SIZE):
        for j in range(SIZE):
            board[i][j] = tmp[i * SIZE + j]

    return board

def initTokens(message):
    tokens = []
    q = deque(list(message))

    while q:
        ch1 = q.popleft()
        ch2 = "X"
        
        if q:
            tmp = q.popleft()
            if ch1 != tmp: ch2 = tmp
            else:
                if ch1 == "X": ch2 = "Q"
                q.appendleft(tmp)
            
        tokens.append(ch1 + ch2)
        
    return tokens

def initTable(board):
    table = {}
    
    for i in range(SIZE):
        for j in range(SIZE):
            table[board[i][j]] = (i, j)
            
    return table

def solution(tokens, board, table):
    encrypt = ""

    for first, second in tokens:
        x1, y1 = table[first]
        x2, y2 = table[second]
        
        if x1 == x2:
            y1 = (y1 + 1) % SIZE
            y2 = (y2 + 1) % SIZE
        elif y1 == y2:
            x1 = (x1 + 1) % SIZE
            x2 = (x2 + 1) % SIZE
        else:
            tmp = y1
            y1 = y2
            y2 = tmp
        
        encrypt += board[x1][y1] + board[x2][y2]
    
    return encrypt

message = input().rstrip()
key = input().rstrip()
board = initBoard(key)
tokens = initTokens(message)
table = initTable(board)

print(solution(tokens, board, table))