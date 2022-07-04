import sys

n = int(input())
timetable = [[0,0]]
for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    timetable.append([t, p])
DP = [0] * (n + 5)

for i in range(1, n+1):
    DP[i] = max(DP[i-1], DP[i])
    DP[i + (timetable[i][0] - 1)] = max(DP[i + (timetable[i][0] - 1)], DP[i-1] + timetable[i][1])
    
print(DP[n])