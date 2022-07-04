from sys import stdin

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
prefix_sum = [0]

tmp = 0
for i in arr:
    tmp += i
    prefix_sum.append(tmp)
    
for n in range(M):
    i, j = map(int, stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])