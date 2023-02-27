import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chicken = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i,j])

def calc(chicken):
    dist = 0
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                min_ = sys.maxsize
                for x, y in chicken:
                    d = abs(i - x) + abs(j - y)
                    min_ = min(min_, d)
                dist += min_
    
    return dist

answer = sys.maxsize
for c in combinations(chicken, M):
    answer = min(answer, calc(c))
    
print(answer)