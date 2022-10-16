import sys
sys.setrecursionlimit(10000000)

def find(x, rooms):
    if x not in rooms:
        rooms[x] = x+1
        return x
    
    rooms[x] = find(rooms[x], rooms)
    return rooms[x]

def solution(k, room_number):
    ans = []
    rooms = {}

    for r in room_number:
        assginment = find(r, rooms)
        ans.append(assginment)
        rooms[assginment] = assginment+1
        
    return ans