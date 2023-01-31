numLi = []

for _ in range(10):
    numLi.append(int(input()))

mxCnt = 0
mxLi = []

for i in set(numLi):
    if numLi.count(i) > mxCnt:
        mxCnt = numLi.count(i)

for j in numLi:
    if numLi.count(j) == mxCnt:
        mxLi.append(j)


print(sum(numLi) // 10)
print(*set(mxLi))