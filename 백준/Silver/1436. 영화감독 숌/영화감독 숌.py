strt = 666
idx = 0
numLi = []
inpt = int(input())

while True:
    if "666" in str(strt):
        numLi.append(strt)
        idx += 1
    strt += 1
    if idx > inpt:
        break

print(numLi[inpt - 1])