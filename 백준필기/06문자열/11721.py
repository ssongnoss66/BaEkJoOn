"""11721 열개씩 끊어 출력하기"""
splitLi = list(input())

while True:
    print("".join(splitLi[:10]))
    if len(splitLi) < 10:
        break
    splitLi = splitLi[10:]

# 리스트 슬라이싱...
