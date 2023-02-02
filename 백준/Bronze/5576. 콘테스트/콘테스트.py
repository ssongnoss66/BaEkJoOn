import sys
inpt = sys.stdin.readline
numLia = []

for i in range(10):
    num = int(inpt())
    if len(numLia) >= 3:
        if min(numLia) < num:
            idx = numLia.index(min(numLia))
            numLia.pop(idx)
            numLia.insert(idx, num)
    else:
        numLia.append(num)

numLib = []

for i in range(10):
    num = int(inpt())
    if len(numLib) >= 3:
        if min(numLib) < num:
            idx = numLib.index(min(numLib))
            numLib.pop(idx)
            numLib.insert(idx, num)
    else:
        numLib.append(num)

print(f"{sum(numLia)} {sum(numLib)}")