"""1316 그룹 단어 체커 https://www.acmicpc.net/problem/1316"""

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

# 리스트[-1] ; 마지막 요소 호출