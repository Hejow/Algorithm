import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(input().split()) if m else list()
ans = abs(100 - n)

for num in range(1000001):
    for x in str(num):
        if x in broken: break
    else:
        ans = min(ans, len(str(num)) + abs(num-n))

print(ans)