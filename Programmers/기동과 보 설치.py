def isCreateable(frame, answer):
    x, y, a, b = frame
    
    if a == 0: # 기둥
        if y == 0: # 바닥
            answer += [x, y, a],
        elif y > 0:
            if [x-1, y, abs(a-1)] in answer or [x, y-1, a] in answer:
                answer += [x, y, a],
    else: # 보
        if y > 0 and (([x, y-1, abs(a-1)] in answer or [x+1, y-1, abs(a-1)] in answer)
                        or ([x-1, y, a] in answer and [x+1, y, a] in answer)):
            answer += [x, y, a],
    
    return True

def isBreakable(frame, answer):
    x, y, a, b = frame
    
    if a == 0: # 기둥
        if [x, y+1, a] in answer:
            return False
    else:
        column = abs(a-1)
        ny = y-1
        
        for i in range(x-1, x+1):
            if [i, ny, column] not in answer:
                return False
        
        for i in range(x+1, x+3):
            if [i, ny, column] not in answer:
                return False
    
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        option = frame[3]
        
        if option == 1: # 설치
            if isCreateable(frame, answer):
                answer += frame[:3],
            
        else: # 삭제
            if isBreakable(frame, answer):
                answer.remove(frame[:3])
            
                    
    return sorted(answer, key=lambda x:(x[0], x[1], -x[2]))