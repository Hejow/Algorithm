places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def check(place):
    people = []
    for i in range(5):
        for j in range(5):
            if (place[i][j] == 'P'):
                people.append([i,j])
                
    for i in range(len(people)-1):
        x1, y1 = people[i]
        for j in range(len(people)):
            x2, y2 = people[j]
            if abs(x1-x2) + abs(y1-y2) <= 2:
                if x1 == x2 or y1 == y2:
                    if place[x1][abs(y2-y1)-1] != 'X' or place[abs(x2-x1)-1][y1] != 'X':
                        return 0
                else:
                    if place[x1][y2] != 'X' or place[x2][y1] != 'X':
                        return 0
        
    return 1
                
def solution(places):
    answer = []
    
    for place in places:
        answer.append(check(place))
    
    return answer