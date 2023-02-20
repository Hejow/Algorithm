answer = 0

def backtracking(cnt, calc, numbers):
    global answer
    size = len(numbers)
    
    if cnt == size:
        if sum(calc) == 0:
            answer += 1
        return
        
    for s in "+-":
        n = s + str(numbers[cnt])
        calc.append(int(n))
        backtracking(cnt+1, calc, numbers)
        calc.pop()

def solution(numbers): # 정수 배열
    calc = []
    backtracking(0, calc, numbers)
    return answer