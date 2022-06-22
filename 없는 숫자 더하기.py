def solution(numbers):
    answer = sum([0,1,2,3,4,5,6,7,8,9])
    answer -= sum(numbers)
        
    return answer