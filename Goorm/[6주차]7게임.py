import sys
input = sys.stdin.readline

nums = [input().strip() for _ in range(5)]

def func(num):
	n = 0
	for i in [0,2,4,6]: n += int(num[i])
	for i in [1,3,5]: 
		if int(num[i]) != 0:
			n *= int(num[i])
	
	return n % 10

for num in nums:
	print(func(num))