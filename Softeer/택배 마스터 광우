from itertools import permutations
import sys
input = sys.stdin.readline

answer = 99999
n, m, k = map(int, input().split())
rails = list(map(int, input().split()))

def calculate(current):
    totalWeight, weight = 0, current[0]
    idx, cnt = 0, 0
    
    while cnt < k:
        nextWeight = current[(idx + 1) % n]
        if weight + nextWeight > m:
            totalWeight += weight
            weight = nextWeight
            cnt += 1
        else:
            weight += nextWeight
        idx += 1
            
    return totalWeight

for p in permutations(rails, n):
    answer = min(answer, calculate(list(p)))

print(answer)