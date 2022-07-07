import sys, itertools
input = sys.stdin.readline

N = int(input())
numbers = []
tmp = []
for _ in range(N):
    num = input().strip()
    numbers.append(num)
    for ch in num:
        if ch not in tmp: tmp.append(ch)
    
max_ = 0
for case in itertools.permutations(tmp, len(tmp)):
    tmp_sum = 0
    for num in numbers:
        for t in tmp:
            num.replace(t, str(case.index(t) + 1))
        tmp_sum += int(num)
        
    max_ = max(max_, tmp_sum)
    
print(max_)
    