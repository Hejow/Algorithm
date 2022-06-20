def solution(board, moves):
    answer = 0
    bucket = []
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] == 0: continue
            if bucket and board[i][m-1] == bucket[-1]:
                bucket.pop()
                answer += 2
            else:
                bucket.append(board[i][m-1])
            board[i][m-1] = 0
            break
        
    return answer