id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
def solution(id_list, report, k):
    answer = []
    result = {}
    new_report = list(set(report))
    fbd_user = []

    for id in id_list:
        result[id] = [[], 0, 0]
    
    for case in new_report:
        tmp = case.split(' ')
        result[tmp[0]][0].append(tmp[1])
        result[tmp[1]][1] += 1    

    for user in id_list:
        if result[user][1] >= k:
            fbd_user.append(user)

    for user in id_list:
        for forbidden in fbd_user:
            if forbidden in result[user][0]:
                result[user][2] += 1
        answer.append(result[user][2])

    return answer

solution(id_list, report, k)