aLi = []
bLi = []

for i in range(3):
    a, b = map(int, input().split())
    aLi.append(a)
    bLi.append(b)

for j in range(3):
    if aLi.count(aLi[j]) == 1:
        aPrint = aLi[j]
    if bLi.count(bLi[j]) == 1:
        bPrint = bLi[j]

print(f"{aPrint} {bPrint}")