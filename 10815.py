from sys import stdin

def binary(arr, left, right, key):
    while left <= right:
        mid = int((left + right) / 2)
        if key > arr[mid]: left = mid + 1
        elif key < arr[mid]: right = mid - 1
        else: return 1
    return 0

n = int(stdin.readline())
N = sorted(map(int, stdin.readline().split()))
m = int(stdin.readline())
M = map(int, stdin.readline().split())

for i in M:
    print(binary(N, 0, n-1, i), end=' ')