def solution(lottos, win_nums):
    zeros, hit = 0, 0
    ranking = [6,6,5,4,3,2,1]
    for l in lottos:
        if l in win_nums: hit+=1
        if l == 0: zeros +=1
    
    return [ranking[hit+zeros], ranking[hit]]