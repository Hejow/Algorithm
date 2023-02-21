import sys
input = sys.stdin.readline

def getServers(n, requests):
    requests = sorted(requests)
    server = 0
    
    smallest = 0
    for request in requests:
        if request > 300: break
        smallest += 1
    
    start = smallest
    end = n-1
    
    while start <= end:
        server += 1
        
        # 큰 값이 600이 넘는 경우
        if requests[end] > 600: pass
        
        # 양쪽 값의 합이 900이하인 경우
        elif start != end and requests[start] + requests[end] <= 900:
            start += 1
        
        # 양쪽 값의 합이 600인 경우
        elif smallest > 0: # 
            smallest -= 1
        end -= 1
    
    # 남아있는 300을 처리
    server += (smallest+2)//3

    return server
    
t = int(input())

for _ in range(t):
    n = int(input())
    requests = list(map(int, input().split()))

    print(getServers(n, requests))