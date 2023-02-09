k, s, n = input().split()
kPlace = list(map(int, [ord(k[0]) - 64, k[1]]))
sPlace = list(map(int, [ord(s[0]) - 64, s[1]]))

dm = {
    "R" : [1, 0],
    "L" : [-1, 0],
    "B" : [0, -1],
    "T" : [0, 1],
    "RT" : [1, 1],
    "LT" : [-1, 1],
    "RB" : [1, -1],
    "LB" : [-1, -1]
}
        
for _ in range(int(n)):
    i = input()
    kx = kPlace[0] + dm[i][0]
    ky = kPlace[1] + dm[i][1]
    if 0 < kx <= 8 and 0 < ky <= 8:
        if [kx, ky] == sPlace:
            # print(f"돌이랑 자리 같아서 돌 이동 전 sPlace {sPlace} kPlace {kPlace}")
            sx = sPlace[0] + dm[i][0]
            sy = sPlace[1] + dm[i][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                sPlace = [sx, sy]
                kPlace = [kx, ky]
                # print(f"돌 이동 후 sPlace {sPlace} kPlace {kPlace}")
            # else:
            #     print(f"체스판 밖으로 나가서 킹돌 이동 없이 sPlace {sPlace} kPlace {kPlace}")
        else:
            kPlace = [kx, ky]
            # print(f"돌이랑 자리 달라서 돌 이동 없이 sPlace {sPlace} kPlace {kPlace}")
    # else:
    #     print(f"체스판 밖으로 나가서 킹돌 이동 없이 sPlace {sPlace} kPlace {kPlace}")

print(f"{chr(kPlace[0] + 64)}{kPlace[1]}")
print(f"{chr(sPlace[0] + 64)}{sPlace[1]}")