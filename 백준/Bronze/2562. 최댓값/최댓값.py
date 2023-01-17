numLi = []
for i in range(9):
    numLi.append(int(input()))

print(max(numLi))
print((numLi.index(max(numLi)))+1)