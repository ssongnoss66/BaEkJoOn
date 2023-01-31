# internetVer

import sys
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
# print(f"arr {arr}")
arr_h = [''.join(i) for i in zip(*arr)]
# print(f"arr_h {arr_h}")
h, v = 0, 0

for i in range(n): 
    for j in arr[i].split('X'):
        if '..' in j:
            h += 1
    for j in arr_h[i].split('X'):
        if '..' in j:
            v += 1

print(h,v)