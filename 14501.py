n = int(input())
arr = []
DP = [0] * n # i 번째 까지의 최대

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    
DP[0] = DP[1] = 0
DP[2] = 10
