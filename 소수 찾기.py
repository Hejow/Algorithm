def solution(n):
    arr = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in arr:
            arr -= set(range(2*i, n+1, i))
    
    return len(arr)

def solution(n):
    answer = 0
    arr = [True] * (n+1)
    
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i+i, n+1, i):
                arr[j] = False
                
    for i in range(2, n+1):
        if arr[i]: answer+=1
    
    return answer