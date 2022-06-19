import re

def solution(new_id):
    answer = re.sub('[^0-9a-z-_.]', '', new_id.lower())
    answer = re.sub('\.{2,}', '.', answer)
    if answer[0] == '.': answer = answer[1:]
    if answer[-1] == '.': answer = answer[:-1]
    answer = 'a' if len(answer) == 0 else answer[:15]
    if answer[-1] == '.': answer = answer[:-1]    
    if len(answer) <= 2: answer = answer + answer[-1] * (3-len(answer)) 
    return answer

solution(new_id[0])