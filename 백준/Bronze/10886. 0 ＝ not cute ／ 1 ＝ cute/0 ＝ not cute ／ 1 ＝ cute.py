n = int(input())
notCute = 0
isCute = 0

for i in range(0, n):
    opinion = int(input())
    if opinion == 0:
        notCute += 1
    elif opinion == 1:
        isCute += 1

if notCute > isCute:
    print("Junhee is not cute!")
elif notCute < isCute:
    print("Junhee is cute!")