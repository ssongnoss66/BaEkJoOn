yearNow = int(input())
if yearNow % 4 == 0:
    if not yearNow % 100 == 0 or yearNow % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)