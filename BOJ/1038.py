from itertools import combinations

n = int(input())

numbers = []
for i in range(1, 11):
    for c in combinations(range(0, 10), i):
        c = list(c)
        c.sort(reverse=True)
        numbers.append(int("".join(map(str, c))))

numbers.sort()

try:
    print(numbers[n])
except:
    print(-1)