import sys
input = sys.stdin.readline

ORDER = ">v<^"
VISITIED = "#"
moves = {
    "^": (-1,0),
    "v": (1,0),
    "<": (0,-1),
    ">": (0,1),
}

a, b = map(int, input().split())
board = [list(input()) for _ in range(a)]

def isValidatePoint(x, y):
    if 0 <= x < a and 0 <= y < b:
        if board[x][y] == VISITIED:
            return True
    return False

def getStartPoint():
    for x in range(a):
        for y in range(b):
            if board[x][y] == VISITIED:
                cnt = 0
                
                for direction in ORDER:
                    nx = x + moves[direction][0]
                    ny = y + moves[direction][1]
                    
                    if isValidatePoint(nx, ny):
                        cnt += 1
                        
                if cnt == 1:
                    return (x, y)

def getDirection(x, y):
    for direction in ORDER:
        nx = x + moves[direction][0]
        ny = y + moves[direction][1]
        
        if isValidatePoint(nx, ny):
            return direction

def getCommand(start, startDirection):
    command = ""
    x, y = start
    currentDirection = startDirection
    
    while True:
        nx = x + moves[currentDirection][0]
        ny = y + moves[currentDirection][1]
        
        if isValidatePoint(nx, ny):
            command += "A"
            x = nx + moves[currentDirection][0]
            y = ny + moves[currentDirection][1]
        else: 
            idx = ORDER.index(currentDirection)
            
            newDirection = currentDirection
            for i in range(1, 4, 2): # 왼쪽 오른쪽
                direction = ORDER[(idx + i) % 4]
                
                nx = x + moves[direction][0]
                ny = y + moves[direction][1]
                
                if isValidatePoint(nx, ny):
                    if i == 1: command += "R"
                    else: command += "L"
                    newDirection = direction

            if currentDirection == newDirection: return command
            else: currentDirection = newDirection

def solution():
    x, y = getStartPoint()
    startDirection = getDirection(x, y)
    command = getCommand((x, y), startDirection)
    
    print(x+1, y+1)
    print(startDirection)
    print(command)

solution()