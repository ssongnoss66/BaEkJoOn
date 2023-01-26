guestN = int(input())
seatNum = list(map(int, input().split()))
seatStack = []
rfs = 0

for i in seatNum:
    if i in seatStack:
            rfs += 1
    else:
        seatStack.append(i)

print(rfs)