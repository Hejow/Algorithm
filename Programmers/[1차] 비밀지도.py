def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1,arr2):
        tmp = str(bin(x|y)[2:])
        tmp = tmp.rjust(n, '0')
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)
    return answer