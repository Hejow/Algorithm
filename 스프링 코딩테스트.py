# def calculateBest(lotteries):
#     arr = []

#     for idx, lotto in enumerate(lotteries, start=1):
#         tmp = []
#         winners, buyer, prize = lotto
        
#         if winners >= buyer+1: tmp.append([100, prize, idx])
#         else: 
#             percent = round(winners/(buyer+1) * 100, 4)
#             tmp.append([percent, prize, idx])

#         arr.extend(tmp)

#     return arr

# def solution(lotteries):
#     arr = calculateBest(lotteries)
    
#     return sorted(arr, key=lambda x:(x[0], x[1]), reverse=True)[0][2]

def isPallindrom(query):
    size = len(query)
    for i in range(size//2):
        if query[i] != query[size-1-i]:
            return False
    
    return True

def isMakeable(query):
    size = len(query)
    half = size//2
    print(size, half)
    for i in range(1, half + 1):
        a, b = query[half - i], query[half + i]
        
        if a - b == 1: # 앞이 더 큰 경우
            return half - i
        elif a - b == -1: # 뒤가 더 큰 경우
            return half + i

    return query.index(max(query))

def gameStart(queries):
    wins = []

    for query in queries:
        tmp = query
        player = 1

        while True:
            idx = isMakeable(tmp)
            tmp[idx] -= 1

            if isPallindrom(tmp):
                wins.append(player)
                break
            
            player = (player + 1) % 2
    
    return wins

def solution(queries):
    return gameStart(queries)

q = [[2,0], [3,1]]

solution(q)