import sys

n, m = map(int, sys.stdin.readline().split())
a1 = set([sys.stdin.readline().strip() for _ in range(n)])
a2 = set([sys.stdin.readline().strip() for _ in range(m)])

a3 = list(a1&a2)

print(len(a3))
for n in sorted(a3):
    print(n)