import sys

S = sys.stdin.readline().strip()
stack = []
result = ''
flag = False

for ch in S:
  if ch == '<':
    if stack:
      while stack:
        result += stack.pop()
    result += ch
    flag = True
  elif ch == '>':
    result += ch
    flag = False
  elif ch == ' ':
    if stack:
      while stack:
        result += stack.pop()
    result += ch
  if ch not in ['<', '>', ' '] and flag: result += ch
  elif ch not in ['<', '>', ' '] and  not flag: stack.append(ch)

if stack:
  while stack:
    result += stack.pop()
      
print(result)