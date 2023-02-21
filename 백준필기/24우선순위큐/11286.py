"""11286 절댓값 힙  https://www.acmicpc.net/problem/11286"""

import sys
inpt = sys.stdin.readline

import heapq
heap = []

for i in range(int(inpt())):
    num = int(inpt())
    if not num == 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)

# abs() ; 절댓값
# heapq.heappop(heap)[1] ; 리스트에서의 pop()과 마찬가지로 반환하고 "삭제"