import sys, collections
input = sys.stdin.readline

def bfs(n, m, board):
    queue = collections.deque()

# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]

wall = 3
cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]