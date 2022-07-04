import sys

n = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for i in range(n)]

def getNum(str):
    res = 0
    for ch in str:
        if ch.isdigit(): res += int(ch)
    return res

arr = sorted(arr, key= lambda x:(len(x), getNum(x), x))

for a in arr:
    print(a)