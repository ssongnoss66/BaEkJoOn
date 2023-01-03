yearNow = int(input())
if yearNow % 4 == 0:
    if not yearNow % 100 == 0 or yearNow % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)

# if not A or B : A가 아니거나! B가 맞거나! 둘 중에 하나만 해당되도 True