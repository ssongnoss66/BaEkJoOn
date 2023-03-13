n, m = map(int, input().split())

ballLi = []

for a in range(n):
    ballLi.append(a+1)

for _ in range(m):
    i, j = map(int, input().split())
    ballLi[i-1], ballLi[j-1] = ballLi[j-1], ballLi[i-1]

print(*ballLi)