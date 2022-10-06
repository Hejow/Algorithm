def solution(msg):
    ans = []
    
    dict = {}
    for idx, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1):
        dict[ch] = idx
    
    tmp = ''
    maxLen = 1
    i = 0
    while i < len(msg):
        for j in range(i+maxLen, i-1, -1):
            tmp = msg[i:j]
            if tmp in dict:
                i = j
                ans.append(dict[tmp])
                break
            
        for k in range(j, len(msg)):
            tmp += msg[k]
            if tmp not in dict:
                maxLen = max(maxLen, len(tmp))
                idx += 1
                dict[tmp] = idx
                tmp = ''
                break
    return ans