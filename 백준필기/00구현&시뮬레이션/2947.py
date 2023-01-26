"""2947 나무 조각"""

numLi = list(map(int, input().split()))

while True:
    for i in range(4):
        if numLi[i] > numLi[i+1]:
            numLi[i], numLi[i+1] = numLi[i+1], numLi[i]
            print(*numLi)
            print(" ".join(map(str, numLi)))
    if numLi == [1, 2, 3, 4, 5]:
        break

# 리스트 요소 위치 변경
# map 함수 활용
# print(* ); 예쁘게 출력!