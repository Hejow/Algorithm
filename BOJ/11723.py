import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    tmp = sys.stdin.readline().split()
    
    if len(tmp) == 1: cmd = tmp[0]
    else: 
        cmd, x = tmp[0], int(tmp[1])
    if cmd == "all": S = set([i for i in range(1, 21)])
    if cmd == 'empty': S = set()
    if cmd == "add": S.add(x)
    if cmd == "remove": S.discard(x)
    if cmd == "check": print(1 if x in S else 0)
    if cmd == "toggle":
        if x in S: S.discard(x)
        else: S.add(x)