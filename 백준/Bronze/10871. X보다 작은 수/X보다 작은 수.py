n, x = map(int, input().split())
numLi = list(map(int, input().split()))
outLi = []

for i in numLi:
    if i < x:
        outLi.append(i)
    
for j in outLi:
    print(j, end=" ")