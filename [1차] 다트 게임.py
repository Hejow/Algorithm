def solution(dartResult):
    result = ''
    flag = False
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if i+2 < len(dartResult):
                if dartResult[i+2] == '#': result += '-1*'
                elif dartResult[i+2] == '*':
                    if i != 0: result += '*2'
                    flag = True
            
            if dartResult[i-1].isdigit(): result += dartResult[i]
            else: result += f'+{dartResult[i]}'
        else: 
            if dartResult[i] == 'T': result += '**3'
            if dartResult[i] == 'D': result += '**2'
            if dartResult[i] == 'S': result += '**1'
            if flag:
                result += '*2'
                flag = False
    return eval(result)