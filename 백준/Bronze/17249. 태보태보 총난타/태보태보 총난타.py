stringLi = list(input().split("(^0^)"))
printLi = []

for string in stringLi:
    printLi.append(str(string.count("@")))

print(" ".join(printLi))