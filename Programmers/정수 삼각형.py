def solution(triangle):
    length = len(triangle)
    
    for i in range(1, length): # 세로
        for j in range(i+1): # 가로
            if j == 0 : triangle[i][0] += triangle[i-1][0]
            elif i == j : triangle[i][j] += triangle[i-1][j-1]
            else: triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
    return max(triangle[length-1])