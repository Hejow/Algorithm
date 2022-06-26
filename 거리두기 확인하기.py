places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX",
     "OXOXP",
     "OXPOX",
     "OXXOP",
     "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]

def check(place):
    people = []
    for i in range(5):
        for j in range(5):
            if (place[i][j] == 'P'):
                people.append([i,j])
                
    for i in range(len(people)-1):
        x1, y1 = people[i]
        for j in range(i+1, len(people)):
            x2, y2 = people[j]
            dist = abs(x1-x2) + abs(y1-y2)
            if dist == 2:
                if x2 == x1:
                    if place[x1][y2-1] == 'O': return 0
                elif y2 == y1:
                    if place[x2-1][y1] == 'O': return 0
                else:
                    if place[x1][y2] == 'O' or place[x2][y1] == 'O': return 0
            elif dist == 1: return 0
    
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(check(place))
    
    return answer

print(solution(places))