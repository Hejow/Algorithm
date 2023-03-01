import sys ; input = sys.stdin.readline

n, m, q = map(int, input().split())
h = [list(map(int, input().split())) for _ in range(m)]
w = list(map(int, input().split()))

nh = [0] * n
s = w[-1]

for i in range(m):
    s += h[i][-1] * w[i]
    for j in range(1, h[i][0]+1):
        nh[h[i][j] - 1] += h[i][j + h[i][0]] * w[i]
        
for _ in range(q):
    inputs = list(map(int, input().split()))
    sum_ = s
    
    for i in range(n):
        sum_ += inputs[i] * nh[i]

    print(sum_)