import sys
inpt = sys.stdin.readline
wrd = input()
dictLi = []

for i in range(len(wrd) - 2):
    a = (wrd[0:(i + 1)])[::-1]
    for j in range((i + 1), (len(wrd) - 1)):
        b = (wrd[(i + 1):(j + 1)])[::-1]
        for k in range((j + 1), (len(wrd))):
            c = (wrd[(j + 1)::])[::-1]
            dictLi.append(a + b + c)

print(sorted(dictLi)[0])