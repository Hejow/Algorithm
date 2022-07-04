from sys import stdin

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
prefix_sum = [sum(arr[:k])]

for i in range(n-k):
    prefix_sum.append(prefix_sum[i] + arr[i+k] - arr[i])
    
print(max(prefix_sum))