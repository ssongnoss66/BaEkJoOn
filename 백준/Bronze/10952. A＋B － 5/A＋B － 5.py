while True:
    hap = sum(int(i) for i in map(int, input().split()))
    if hap == 0:
        break
    print(hap)