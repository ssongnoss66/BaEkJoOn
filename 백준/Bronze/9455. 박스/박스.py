for i in range(int(input())):
    m, n = map(int, input().split())
    garo = [input().rstrip() for _ in range(m)]
    sero = ["".join(i) for i in zip(*garo)]
    hap = 0
    for j in sero:
        li = list(j)
        cnt = li.count("1")
        num = (len(li) - cnt)
        # print(f"li {li}일 때 리스트 안에 1은 {cnt}개 있고 리스트의 길이인 5에서 1의 갯수 {cnt}를 뺀 {num}으로 인덱스 위치를 바꿔준다")
        for k in range(len(li)):
            if li[k] == "1":
                hap += (num - k)
                # print(f"k의 인덱스 {k}를 {num}으로 옮기기 위해서 {num - (k)}칸을 움직여야 하고 지금까지 {hap} 칸 움직임")
                num += 1
    print(hap)