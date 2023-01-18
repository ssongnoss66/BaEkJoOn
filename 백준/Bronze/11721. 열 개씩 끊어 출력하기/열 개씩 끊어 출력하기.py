splitLi = list(input())

while True:
    print("".join(splitLi[:10]))
    if len(splitLi) < 10:
        break
    splitLi = splitLi[10:]