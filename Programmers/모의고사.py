def solution(answers):
    answer, score = [], []
    cases = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    for case in cases:
        cnt, idx = 0, 0
        for i in range(len(answers)):
            if answers[i] == case[idx]: cnt+=1
            if idx == len(case)-1 : idx = 0
            else: idx += 1
        score.append(cnt)
    
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
    
    return answer