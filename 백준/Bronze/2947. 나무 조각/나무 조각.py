numLi = list(map(int, input().split()))

while True:
    for i in range(4):
        if numLi[i] > numLi[i+1]:
            numLi[i], numLi[i+1] = numLi[i+1], numLi[i]
            print(" ".join(map(str, numLi)))
    if numLi == [1, 2, 3, 4, 5]:
        break
