"""9093 단어뒤집기"""

t = int(input())

for i in range(t):
    sentenceLi = map(str, input().split())
    reverseLi = []
    for j in sentenceLi:
        reverseLi.append(j[::-1])
    print(" ".join(reverseLi))

# 문자열 슬라이싱 문자열[::-1]