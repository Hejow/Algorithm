from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    tmp = list(input().split())
    if tmp[0] == '0': break
    
    for c in combinations(tmp[1:], 6):
        print(' '.join(c))
        
    print()