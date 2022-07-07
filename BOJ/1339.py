import sys

N = int(sys.stdin.readline())
numbers = []
dict = {}

for _ in range(N):
    tmp = sys.stdin.readline().strip()
    numbers.append(tmp)
    for idx, x in enumerate(tmp):
        dict[x] = dict.get(x, 0) + 10 ** (len(tmp) - idx - 1)
        
dict_values = list(dict.values())
dict_values.sort(reverse=True)

answer = 0
for i, x in enumerate(dict_values):
    answer += x * (9-i)
    
print(answer)