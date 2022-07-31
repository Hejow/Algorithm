import sys, itertools
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_ = 0
for c in itertools.permutations(arr,N):
    tmp = 0
    for i in range(N-1):
        tmp += abs(c[i] - c[i+1])
    
    max_ = max(max_, tmp)

print(max_)