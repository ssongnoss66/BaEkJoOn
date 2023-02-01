strt = 4
strtSt = set(str(strt).strip())
idx = 0
numLi = []
inpt = int(input())

while True:
    if strtSt == {"4"} or strtSt == {"7"} or strtSt == {"4", "7"}:
        numLi.append(strt)
        idx += 1
    strt += 1
    strtSt = set(str(strt).strip())
    if numLi[idx - 1] > inpt:
        break

print(numLi[idx-2])