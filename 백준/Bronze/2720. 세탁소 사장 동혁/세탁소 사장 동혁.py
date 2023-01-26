for i in range(int(input())):
    chng = int(input())
    q = chng // 25
    chng = chng % 25
    d = chng // 10
    chng = chng % 10
    n = chng // 5
    p = chng % 5
    print(f"{q} {d} {n} {p}")