inptLi = []

while True:
    wrd = input()
    if wrd == "고무오리 디버깅 시작":
        pass
    elif wrd == "고무오리 디버깅 끝":
        if inptLi.count("문제") == 0:
            print("고무오리야 사랑해")
            break
        else:
            print("힝구")
            break
    else:
        if wrd == "문제":
            inptLi.append(wrd)        
        elif wrd == "고무오리":
            if inptLi.count("고무오리") + 1 > inptLi.count("문제"):
                inptLi.append("문제")
                inptLi.append("문제")
            else:
                inptLi.remove(inptLi[0])