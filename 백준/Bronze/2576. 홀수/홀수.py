oddNum = []

for i in range(7):
    num = int(input())
    if num % 2 == 1:
        oddNum.append(num)  

if len(oddNum) > 0:
    print(sum(oddNum))
    print(min(oddNum))
else:
    print(-1)