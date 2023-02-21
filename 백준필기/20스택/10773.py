"""10773 제로 https://www.acmicpc.net/problem/10773"""

numLi = []

for k in range(int(input())):
    num = int(input())
    if num == 0:
        numLi.pop()
    else:
        numLi.append(num)

print(sum(numLi))

# 리스트명.pop() ; 마지막 요소 삭제