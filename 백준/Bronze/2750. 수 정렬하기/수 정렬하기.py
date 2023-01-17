n = int(input())
numLi = []

for i in range(n):
    numLi.append(int(input()))

for j in sorted(numLi):
    print(j)