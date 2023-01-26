numLi = []

for i in range(1, int(input())+1):
    numLi.append(i)

prntLi = []

while True:
    if len(numLi) == 1:
        break
    prntLi.append(numLi[0])
    del numLi[0]
    numLi.append(numLi[0])
    del numLi[0]
    

prntLi.append(numLi[0])
print(*prntLi)