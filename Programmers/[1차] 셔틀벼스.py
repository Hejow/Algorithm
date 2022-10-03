def convert(time):
    if type(time) == int:
        h = time // 60
        m = time % 60 
        return str(h).zfill(2) + ":" + str(m).zfill(2)
    else:
        h, m = time.split(":")
        return int(h) * 60 + int(m)

def solution(n, t, m, timetable):
    # 셔틀 버스 시간
    shuttleBus = convert("09:00")
    
    newTimetable = [convert(time) for time in timetable]
    newTimetable.sort()

    # 마지막에 탄 사람 시간, 마지막 버스에 탄 사람 수
    lastCrew, lastCnt = 0, 0
    
    for _ in range(n):
        cnt = 0
        while newTimetable and cnt < m and newTimetable[0] <= shuttleBus:
            lastCrew = newTimetable.pop(0)
            cnt += 1
            
        lastCnt = cnt
        shuttleBus += t
    
    return convert(lastCrew - 1) if lastCnt == m else convert(shuttleBus - t)