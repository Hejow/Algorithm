def solution(play_list, listen_time):
    size = len(play_list)
    max_ = 0
    
    for i in range(size):
        givenTime = listen_time
        tmp = []
        idx = i+1
        
        tmp.append(i)
        givenTime -= 1
        
        while True:
            if (idx % size) in tmp: return size
            
            playTime = play_list[idx % size]
            givenTime -= playTime
            tmp.append((idx % size))
            idx += 1
            
            if givenTime <= 0: break
        
        max_ = max(max_, len(tmp))
    
    return max_

play_list = [1,3,5,7,3]
listen_time = 3

print(solution(play_list, listen_time))