"""17249 태보태보 총난타"""

stringLi = list(input().split("(^0^)"))
printLi = []

for string in stringLi:
    printLi.append(str(string.count("@")))

print(" ".join(printLi))

# "".join(리스트명)