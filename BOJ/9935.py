import sys

S = sys.stdin.readline().strip()
Boom = sys.stdin.readline().strip()

stack = []
for ch in S:
    stack.append(ch)
    if ''.join(stack[-len(Boom):]) == Boom: 
       del stack[-len(Boom):]
    
if stack: print(''.join(stack))
else: print('FRULA')