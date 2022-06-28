expression = "100-200*300-500+20"

def toList(expression):
    result = []
    op = []
    tmp = ''
    for ch in expression:
        if ch.isdigit(): tmp += ch
        else:
            result.append(tmp)
            result.append(ch)
            op.append(ch)
            tmp = ''
    result.append(tmp)
            
    return result, set(op)

def solution(expression):
    answer = 0
    exp, op = toList(expression)   
    
    return answer