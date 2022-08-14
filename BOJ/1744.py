N = int(input())
positive, negative = [], []
one = []

for _ in range(N):
    tmp = int(input())
    if tmp > 1: positive.append(tmp)
    elif tmp <= 0: negative.append(tmp)
    else: one.append(tmp)
    
positive.sort(reverse=True)
negative.sort()

result = sum(one)

def solution(array):
    global result
    
    l = len(array)
    for i in range(0, l, 2):
        if i == l-1:
            result += array[i]
            break
        result += array[i] * array[i+1]
    
for arr in [positive, negative]:
    solution(arr)

print(result)