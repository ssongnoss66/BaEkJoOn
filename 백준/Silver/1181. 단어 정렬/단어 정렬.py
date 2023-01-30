import heapq
heap = []
num = int(input())
for i in range(num):
    wrd = input()
    if not (len(wrd), wrd) in heap:
        heapq.heappush(heap, (len(wrd), wrd))

for j in range(num):
    try:
        print(heapq.heappop(heap)[1])
    except:
        break