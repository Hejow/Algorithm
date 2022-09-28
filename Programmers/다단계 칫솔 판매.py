def solution(enroll, referral, seller, amount):
    ans = [0] * len(enroll)
    
    dict = {}
    for i, e in enumerate(enroll):
        dict[e] = i
        
    for s, a in zip(seller, amount):
        profit = a * 100
        
        while s != '-' and profit > 0:
            idx = dict[s]
            ans[idx] += profit - profit//10
            profit //= 10
            s = referral[idx]
            
    return ans