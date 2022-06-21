import sys
import statistics

n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for i in range(n)]
dict = {}

for i in num:
    if i in dict: dict[i] += 1
    else: dict[i] = 1
    
max_cnt = max(dict.values())
for i in num:
    if i in dict and dict[i] != max_cnt:
        del dict[i]
        
mode = sorted(dict)[0] if len(dict.keys()) == 1 else sorted(dict)[1]
# if len(dict.keys()) == 1:
#     mode = sorted(dict)[0]
# else : mode = sorted(dict)[1]

print(round(statistics.mean(num)))
print(sorted(num)[int((n+1)/2-1)])
print(mode)
print(max(num) - min(num))