"""2161 카드1 https://www.acmicpc.net/problem/2161"""

# ssaemVer ; queue

n = int(input())
queue = list(range(1, n + 1))

while len(queue) > 1:
    print(queue.pop(0), end = " ")
    queue.append(queue.pop(0))

print(queue[0])

# ssaemVer ; Deque

from collections import deque

n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
    print(queue.popleft(), end=" ")
    queue.append(queue.popleft())

print(queue[0])

# myVer
n = int(input())
numLi = list(range(1, n+1))

prntLi = []

while True:
    if len(numLi) == 1:
        break
    prntLi.append(numLi[0])
    del numLi[0]
    numLi.append(numLi[0])
    del numLi[0]
    

prntLi.append(numLi[0])
print(*prntLi)

# 범위에 해당하는 리스트 만들기 numLi = list(range(1, int(input())+1))