SIZE = 3
CIRCLE = "O"
X = "X"
BLANK = "."

def countOX(board):
    cntO, cntX = 0, 0
    
    for i in range(SIZE):
        cntO += board[i].count(CIRCLE)
        cntX += board[i].count(X)
        
    return cntO, cntX

def countLineOX(board):
    cntOl, cntXl = 0, 0
    
    # 가로 따지기
    for b in board:
        if "OOO" == b: cntOl += 1
        elif "XXX" == b: cntXl += 1
    
    # 세로 따지기
    for y in range(SIZE):
        t = board[0][y]
        if t == BLANK: continue
        if t == board[1][y] and t == board[2][y]:
            if t == CIRCLE: cntOl += 1
            else: cntXl += 1
        
    # 대각선 따지기
    for i in range(0, SIZE, 2):
        t = board[0][i]
        if t == BLANK: continue
        if t == board[1][1] and t == board[2][2-i]:
            if t == CIRCLE: cntOl += 1
            else: cntXl += 1
            
    return cntOl, cntXl

def solution(board):
    cntO, cntX = countOX(board)
    cntOl, cntXl = countLineOX(board)
    
    if cntOl + cntXl > 1:
        if cntOl > 1 and cntO - cntX == 1: return 1
        return 0

    if cntXl == 1 and cntO > cntX: return 0
    if cntOl == 1 and cntO == cntX: return 0
    
    return 1

t = 	["...", ".X.", "..."]
print(solution(t))