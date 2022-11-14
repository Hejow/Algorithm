import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
ans = ''

for i in range(0, n-1, 2):
	ch = ord(s[i])
	digit = int(s[i+1]) ** int(s[i+1])
	ans += chr((ch + digit) % 122)

print(ans)