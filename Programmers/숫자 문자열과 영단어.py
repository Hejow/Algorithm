numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    answer = s
    for i in range(10):
        answer = answer.replace(numbers[i], str(i))
    
    return int(answer)