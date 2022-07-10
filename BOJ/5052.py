import sys
input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
n = int(input())
d = {}
for _ in range(n):
    tmp = int(input())
    l = len(str(tmp))
    d[l] = d.get(l, []) + [tmp]
    
print(d)