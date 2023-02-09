import sys
input = sys.stdin.readline

moves = [(1,0), (0,1), (-1,0), (0,-1)]

n, m, q = map(int, input().split())

seats = [[0 for _ in range(m)] for _ in range(n)]

checkTable = {} 
eatingUsers = set()

def checkUser(id):
    if id not in checkTable:
        return "NEW"
    return checkTable[id][0]

def getAvailableSeat():
    if (len(eatingUsers) == 0):
        return (0, 0)
    
    x, y = -1, -1
    copied = [seat[:] for seat in seats]

    for i in range(n):
        for j in range(m):
            if copied[i][j] == 0:
                minDistance = int(1e9)
                for u in eatingUsers:
                    a, b = checkTable[u][1]
                    minDistance = min(minDistance, (i-a)**2 + (j-b)**2)
                copied[i][j] = minDistance
    
    safePoint = max(map(max, copied))
    
    if safePoint != 1:
        arr = []
        for x in range(n):
            for y in range(m):
                if copied[x][y] == safePoint:
                    arr.append([x, y])
        x, y = sorted(arr, key=lambda x:(x[0], x[1]))[0]
            
    return x, y

def takeSeat(id, seat):
    eatingUsers.add(id)
    checkTable[id] = ["EAT", seat]
    x, y = seat
    seats[x][y] = 1
    
    for i in range(4):
        nx = x + moves[i][0]
        ny = y + moves[i][1]
        
        if 0 <= nx < n and 0 <= ny < m:
            seats[nx][ny] = -1
    
    print(f"{id} gets the seat ({x+1}, {y+1}).")

def leaveSeat(id):
    eatingUsers.remove(id)
    x, y = checkTable[id][1]
    checkTable[id][0] = "ATE"
    seats[x][y] = 0
    
    for i in range(4):
        nx = x + moves[i][0]
        ny = y + moves[i][1]
        
        if 0 <= nx < n and 0 <= ny < m:
            seats[nx][ny] = 0
    
    print(f"{id} leaves from the seat ({x+1}, {y+1}).")

def inCommand(id):
    status = checkUser(id)
    if status == "NEW":
        seat = getAvailableSeat()
        if seat[0] == -1 and seat[1] == -1:
            print("There are no more seats.")
            return
        
        takeSeat(id, seat)
    elif status == "EAT":
        print(f"{id} already seated.")
    elif status == "ATE":
        print(f"{id} already ate lunch.")

def outCommand(id):
    status = checkUser(id)
    if status == "NEW":
        print(f"{id} didn't eat lunch.")
    elif status == "EAT":
        leaveSeat(id)
    elif status == "ATE":
        print(f"{id} already left seat.")

for _ in range(q):
    command, id = input().split()
    inCommand(int(id)) if command == "In" else outCommand(int(id))