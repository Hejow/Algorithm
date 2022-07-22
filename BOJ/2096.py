import sys

input = sys.stdin.readline
n = int(input())

DP_max = [0] * 3
DP_min = [0] * 3

max_ = [0] * 3
min_ = [0] * 3

for x in range(n):
    a, b, c = map(int, input().split())
    for y in range(3):
        if y == 0:
            max_[y] = a + max(DP_max[y], DP_max[y + 1])
            min_[y] = a + min(DP_min[y], DP_min[y + 1])
        if y == 1:
            max_[y] = b + max(DP_max[y - 1], DP_max[y], DP_max[y + 1])
            min_[y] = b + min(DP_min[y - 1], DP_min[y], DP_min[y + 1])
        if y == 2:
            max_[y] = c + max(DP_max[y], DP_max[y - 1])
            min_[y] = c + min(DP_min[y], DP_min[y - 1])

    for y in range(3):
        DP_max[y] = max_[y]
        DP_min[y] = min_[y]

print(max(DP_max), min(DP_min))