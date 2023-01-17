inputNum = int(input())
num = inputNum
circ = 0

while True:
    leftNum = num // 10
    if num < 10:
        leftNum = 0
    rightNum = num % 10
    if rightNum + leftNum >= 10:
        newNum = (rightNum * 10) + ((rightNum + leftNum) % 10)
    elif rightNum + leftNum < 10:
        newNum = (rightNum * 10) + (rightNum + leftNum)
    circ += 1
    if inputNum == newNum:
        break
    num = newNum

print(circ)