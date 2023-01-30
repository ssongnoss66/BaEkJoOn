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