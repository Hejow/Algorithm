def solution(n, lost, reserve):
    reserve_ = [r for r in reserve if r not in lost]
    lost_ = [l for l in lost if l not in reserve]
    reserve_.sort()
    
    for r in reserve_:
        if r-1 in lost_: lost_.remove(r-1)
        elif r+1 in lost_: lost_.remove(r+1)
                    
    return n - len(lost_)