garo = [input().rstrip() for _ in range(5)]

if not len(min(garo, key=len)) == len(max(garo, key=len)):
    for i in garo:
        mxLn = len(max(garo, key=len))
        if mxLn > len(i):
            indx = garo.index(i)
            for j in range(mxLn - len(i)):
                i = i + "*"
            garo[indx] = i

sero = ["".join(i) for i in zip(*garo)]

print(("".join(sero)).replace("*",""))