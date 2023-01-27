a, b, c = map(int, input().split())

try:
    if (a // (c-b)) >= 0:
        print((a // (c-b))+1)
    else:
        print(-1)
except:
    print(-1)