N = int(input())
positiveList = []
negativeList = []
oneList = []

for _ in range(N):
    tmp = int(input())
    if tmp > 1: positiveList.append(tmp)
    elif tmp <= 0: negativeList.append(tmp)
    else: oneList.append(tmp)
    
positiveList.sort(reverse=True)
negativeList.sort()

result = 0

if len(positiveList) % 2 == 0:
    for i in range(0, len(positiveList), 2):
        result += positiveList[i] * positiveList[i+1]
else:
    for i in range(0, len(positiveList)-1, 2):
        result += positiveList[i] * positiveList[i+1]
    result += positiveList[-1]
    
if len(negativeList) % 2 == 0:
    for i in range(0, len(negativeList), 2):
        result += negativeList[i] * negativeList[i+1]
else:
    for i in range(0, len(negativeList)-1, 2):
        result += negativeList[i] * negativeList[i+1]
    result += negativeList[-1]
    
result += sum(oneList)

print(result)