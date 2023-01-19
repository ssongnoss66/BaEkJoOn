commuteSet = set()

for i in range(int(input())):
    k, v = input().split()
    if v == "enter":
        commuteSet.add(k)
    else:
        commuteSet.remove(k)

for j in sorted(commuteSet)[::-1]:
    print(j)