import sys
input = sys.stdin.readline

N = int(input())
crains = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

crains.sort(reverse=True)
boxes.sort(reverse=True)

cnt = 0