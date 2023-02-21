"""2908 상수 https://www.acmicpc.net/problem/2908"""

a, b = map(str, input().split())
srtA = a[::-1]
srtB = b[::-1]

if int(srtA) > int(srtB):
    print(srtA)
else:
    print(srtB)

# 문자열[::-1] ; 역순 출력