import sys
input = sys.stdin.readline

dict = {
    '1': ['i', 'j'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h'],
    '5': ['k', 'l'],
    '6': ['m', 'n'],
    '7': ['p', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y'],
    '0': ['o', 'q', 'z']
}

phone_num = input().strip()
n = int(input())
words = []
min_ = 101
result = []

for _ in range(n): 
    str = input().strip()
    tmp = ''
    for ch in str:
        for key in '1234567890':
            if ch in dict[key]: tmp += key
    words.append([tmp, str])

def Backtracking(arr, cnt):
    global result, min_
    if cnt == len(phone_num) and len(arr) < min_:
        min_ = len(arr)
        result.clear()
        result += arr
        return
    
    for w in words:
        if w[0] == phone_num[cnt:cnt+len(w[0])]:
            arr.append(w[1])
            Backtracking(arr, cnt+len(w[0]))
            arr.remove(w[1])
            
arr = []
Backtracking(arr, 0)

if result:
    print(len(result))
    for r in result:
        print(r)
else:
    print(0)
    print('No solution.')