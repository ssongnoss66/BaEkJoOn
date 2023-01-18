t = int(input())

for i in range(t):
    sentenceLi = map(str, input().split())
    reverseLi = []
    for j in sentenceLi:
        reverseLi.append(j[::-1])
    print(" ".join(reverseLi))