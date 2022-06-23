def isCorrect(str):
    test = []
    for element in str:
        if len(test) == 0: test.append(element)
        elif test[-1] == '(' and element == ')': test.pop()
        else: test.append(element)
        
    return True if len(test) == 0 else False

def seperateStr(str):
    l = r = 0
    for i in range(len(str)):
        if str[i] == '(': l +=1
        else: r+=1
        if l == r:
            return str[:i+1], str[i+1:]
    
def reverseStr(str):
    tmp = ''
    for ch in str:
        if ch == ')': tmp += '('
        else: tmp += ')'
    return tmp
    
def solution(p):
    answer = ''
    if isCorrect(p): answer += p
    else: 
        u, v = seperateStr(p)
        if isCorrect(u):
            u += solution(v)
            answer += u
        else:
            u = reverseStr(u[1:len(u)-1])
            tmp = '(' + solution(v) + ')' + u
            answer += tmp
        
    return answer