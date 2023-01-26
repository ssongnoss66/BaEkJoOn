"""2675 문자열 반복"""

trial = int(input())

for i in range(trial):
    inputLi = list(map(str, input().split()))
    r = int(inputLi[0])
    word = inputLi[1]
    printLi = []
    for j in range(len(word)):
        printLi.append(word[j]*r)
    print("".join(printLi))
        
# "".join(리스트명)