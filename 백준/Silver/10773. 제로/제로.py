numLi = []

for k in range(int(input())):
    num = int(input())
    if num == 0:
        numLi.pop()
    else:
        numLi.append(num)

print(sum(numLi))