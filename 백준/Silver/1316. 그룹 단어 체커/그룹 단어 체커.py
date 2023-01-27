prntCnt = 0

for i in range(int(input())):
    inptLi = []
    for j in input().strip():
        try:
            if inptLi[-1] == j:
                pass
            elif not inptLi[-1] == j:
                inptLi.append(j)
        except:
            if j not in inptLi:
                inptLi.append(j)
    prntWrd = ""
    for k in inptLi:
        if inptLi.count(k) == 1:
            prntWrd = "T"
        else:
            prntWrd = "F"
            break
    if prntWrd == "T":
        prntCnt += 1

print(prntCnt)