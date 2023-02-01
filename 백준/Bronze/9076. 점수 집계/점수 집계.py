import sys
inpt = sys.stdin.readline

for i in range(int(inpt())):
    numLi = list(map(int, input().split()))
    mx = max(numLi)
    mn = min(numLi)
    numLi.remove(mx)
    numLi.remove(mn)
    if max(numLi) - min(numLi) >= 4:
        print("KIN")
    else:
        print(sum(numLi))