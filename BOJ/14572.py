import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
# 학생들의 정보 => 학생 실력, 알고있는 알고리즘
students = []
# 해당 알고리즘 아는 학생 수
algorithms = [0 for _ in range(K+1)]

for _ in range(N):
    student = [int(input().split()[-1])]
    student.append(list(map(int, input().split())))
    students.append(student)
students.sort()

start, end, E = 0, 0, 0

while start < N:
    while end < N and students[end][0] - students[start][0] <= D:
        for i in students[end][1]:
            algorithms[i] += 1
        end += 1
        
    anyKnows, allKnows = 0, 0
    for i in range(1, K+1):
        if algorithms[i] != 0:
            if algorithms[i] == end - start:
                allKnows += 1
            anyKnows += 1
            
    E = max(E, (anyKnows - allKnows) * (end - start))
    
    for i in students[start][1]:
        algorithms[i] -= 1
    start += 1
    
print(E)