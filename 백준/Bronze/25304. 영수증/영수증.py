totalX = int(input())
typeN = int(input())
hapTotal = 0
rnd = 1

while rnd <= typeN:
    (price, num) = map(int, input().split())
    hapItem = price*num
    hapTotal += hapItem
    rnd += 1
    if rnd > typeN:
        break

if totalX==hapTotal:
    print("Yes")
else:
    print("No")