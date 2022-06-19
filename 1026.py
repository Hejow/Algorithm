num = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0

a.sort()
b.sort(reverse=True)

for i in range(num):
    sum = sum + a[i] * b[i]
    
print(sum)