a = int(input())
b = int(input())
c = int(input())
abc = a*b*c
numDict = {}

for i in range(0, 10):
    numDict[i] = str(abc).count(str(i))

print("\n".join(map(str, numDict.values())))