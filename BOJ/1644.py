N = int(input())

prime_nums = [True] * (N+1)
for i in range(2, int(N**0.5)+1):
    if prime_nums[i]:
        for j in range(i+i, (N+1), i):
            prime_nums[j] = False
  
end, sum_, cnt = 2, 0, 0

for start in range(2, N+1):
    if not prime_nums[start]: continue
    while sum_ < N and end < N+1:
        if not prime_nums[end]: 
            end += 1
            continue
        sum_ += end
        end += 1
    if sum_ == N: cnt += 1
    sum_ -= start
    
print(cnt)        