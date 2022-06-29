import itertools

def toList(expression):
    exp, op = [], []
    tmp = ''
    for ch in expression:
        if ch.isdigit(): tmp += ch
        else:
            exp.append(tmp)
            exp.append(ch)
            if ch not in op: op.append(ch)
            tmp=''
    exp.append(tmp)
    
    return exp, op

def toPost(priority, tokens):
    list_ = []
    stack = []
    
    for token in tokens:
        if token.isdigit(): list_.append(token)
        else:
            while len(stack) != 0 and priority.index(token) >= priority.index(stack[-1]): 
                list_.append(stack.pop())
            stack.append(token)
                    
    for i in range(len(stack)):
        list_.append(stack.pop())
    
    return list_

def calc(tokens):
    stack = []
    for token in tokens:
        if token.isdigit(): stack.append(token)
        elif len(stack) > 1 :
            b = int(stack.pop())
            a = int(stack.pop())
            if token == '*':
                stack.append(a*b)
            elif token == '+':
                stack.append(a+b)  
            elif token == '-':
                stack.append(a-b)
            
    return abs(stack.pop())

def solution(expression):
    answer = 0
    exp, op = toList(expression)
    for priority in itertools.permutations(op, len(op)):
        answer = max(answer, calc(toPost(priority,exp)))
        
    return answer

# def calc(priorities, n, expression):
#     if n == 2: return str(eval(expression))
#     if priorities[n] == '*':
#         result = eval('*'.join([calc(priorities, n+1, exp) for exp in expression.split('*')]))
#     if priorities[n] == '+':
#         result = eval('+'.join([calc(priorities, n+1, exp) for exp in expression.split('+')]))
#     if priorities[n] == '-':
#         result = eval('-'.join([calc(priorities, n+1, exp) for exp in expression.split('-')]))
#     return str(result)

# def solution(expression):
#     answer = 0
#     for priorities in permutations(['+', '-', '*'], 3):
#         result = int(calc(priorities, 0 ,expression))
#         answer = max(answer, abs(result))
        
#     return answer