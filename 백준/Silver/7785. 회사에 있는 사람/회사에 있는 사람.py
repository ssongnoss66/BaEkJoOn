n = int(input())
commuteDict = {}

for i in range(n):
    k, v = map(str, input().split())
    commuteDict[k] = v

printLi = []
for k, v in commuteDict.items():
    if v == "enter":
        printLi.append(k)

for j in sorted(printLi, reverse=True):
    print(j)