"""1157 단어 공부 https://www.acmicpc.net/problem/1157"""

strng = input().upper()
mxCnt = 0
mxWrd = ""
for i in set(strng):
    num = strng.count(i)
    if num > mxCnt:
        mxCnt = num
        mxWrd = i
    elif num == mxCnt:
        mxCnt = num
        mxWrd = "?"
    else:
        continue

print(mxWrd)

"""

시간초과

import sys
inpt = sys.stdin.readline()

inptStr = inpt.upper()
inptDi = {}

for i in inptStr:
    inptDi[i] = inptStr.count(i)

prntLi = [k for k,v in inptDi.items() if max(inptDi.values()) == v]

if len(prntLi) > 1:
    print("?")
else:
    print(prntLi[0])

# 딕셔너리 최대값에 해당하는 키 반환 prntLi = [k for k,v in inptDi.items() if max(inptDi.values()) == v]

"""