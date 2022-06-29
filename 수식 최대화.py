import itertools

def toList(expression):
    exp = []
    op = []
    tmp = ''
    
    for ch in expression:
        if ch.isdigit(): tmp += ch
        else:
            exp.append(tmp)
            exp.append(ch)
            tmp = ''
            op.append(ch)
    exp.append(tmp)
    
    return exp, list(set(op))

def calc(exp, case):
    list_ = []
    stack = []
    for i in range(len(exp)):
        if exp[i].isdigit():list_.append(exp[i])
        else:
            if len(stack) == 0 : stack.append(exp[i])
            else:
                if case[stack[-1]] > case[exp[i]]: 
                    list_.append(stack.pop())
                    stack.append(exp[i])
                else: stack.append(exp[i])
    for i in range(len(stack)):
        list_.append(stack.pop())
        
    return list_
                    

def solution(expression):
    answer = 0
    exp, op = toList(expression)
    
    cases = []
    for case in itertools.permutations(op, len(op)):
        obj = {}
        for c, i in zip(case, [3,2,1]):
            obj[c] = i
        cases.append(obj)
        
    return answer