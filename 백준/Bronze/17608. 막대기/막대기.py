import sys
input = sys.stdin.readline

num = int(input())
stckLi = []

for i in range(num):
    stckLi.append(int(input()))

stndrd = stckLi.pop()
stckLi = list(reversed(stckLi))
prnt = 1
mx = 0

# print(f"stndrd {stndrd} stckLi {stckLi}")

for j in stckLi:
    if stndrd < j and mx < j:
        prnt += 1
        mx = j

print(prnt)