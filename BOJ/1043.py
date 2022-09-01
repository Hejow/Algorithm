import sys
input = sys.stdin.readline

n, m = map(int, input().split())
whoKnows = set(input().split()[1:])
parties = []
ans = 0

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & whoKnows:
            whoKnows = whoKnows.union(party)

for party in parties:
    if party & whoKnows:
        continue
    ans += 1

print(ans)