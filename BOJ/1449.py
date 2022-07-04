import sys

n, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
cnt = 0

if l == 1: 
    print(len(arr))
    sys.exit(0)
while len(arr) != 0:
    tmp = arr[0]
    cnt += 1
    for i in range(l):
        if tmp+i in arr: arr.remove(tmp+i)
        
print(cnt)