a, b = map(str, input().split())
srtA = a[::-1]
srtB = b[::-1]

if int(srtA) > int(srtB):
    print(srtA)
else:
    print(srtB)