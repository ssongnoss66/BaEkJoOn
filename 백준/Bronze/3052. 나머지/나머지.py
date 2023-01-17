remainderSet = set()

for i in range(10):
    remainder = (int(input())) % 42
    remainderSet.add(remainder)

print(len(remainderSet))