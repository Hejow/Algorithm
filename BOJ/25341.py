# import sys
# input = sys.stdin.readline

# n, m, q = map(int, input().split())
# h = [list(map(int, input().split())) for _ in range(m)]
# w = list(map(int, input().split()))

# for _ in range(q):
#     inputs = list(map(int, input().split()))
#     sum_ = w[-1] # 편향값
    
#     for i in range(m):
#         tmp = h[i][-1] # 편향값
        
#         for j in range(1, h[i][0] + 1):
#             tmp += inputs[h[i][j] - 1] * h[i][j + h[i][0]]

#         sum_ += tmp * w[i]
    
#     print(sum_)
t = 1
t += 1 * 2
print(t)