numbers, hands = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"

def getDistance(l_idx, r_idx, target):
    l_dist = abs(l_idx[0] - target[0]) + abs(l_idx[1] - target[1])
    r_dist = abs(r_idx[0] - target[0]) + abs(r_idx[1] - target[1])
    
    return l_dist - r_dist

def solution(numbers, hand):
    answer = ''
    l_pos, r_pos = '*', '#'
    keypads = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['*','0','#']
    ]
        
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            l_pos = str(num)
        elif num in [3,6,9]:
            answer += 'R'
            r_pos = str(num)
        else:
            if num not in ['*', '0', '#']:
                l_idx = (int(l_pos)-1)//3, keypads[(int(l_pos)-1)//3].index(l_pos)
                r_idx = (int(r_pos)-1)//3, keypads[(int(r_pos)-1)//3].index(r_pos)
                num_idx = (num-1)//3, keypads[(num-1)//3].index(str(num))
            else:
                l_idx = 3, keypads[3].index(l_pos)
                r_idx = 3, keypads[3].index(r_pos)
                num_idx = 3, 1
            
            if getDistance(l_idx, r_idx, num_idx) < 0: 
                answer+= 'L'
                l_pos = str(num)
            elif getDistance(l_idx, r_idx, num_idx) > 0:
                answer+= 'R'
                r_pos = str(num)
            else:
                if hand == 'left':
                    answer+= 'L'
                    l_pos = str(num)
                else:
                    answer+= 'R'
                    r_pos = str(num)
                    
    return answer

print(solution(numbers, hands))