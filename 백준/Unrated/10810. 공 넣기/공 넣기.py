n, m = map(int, input().split())

ballLi = []

for _ in range(n):
    ballLi.append(0)

for _ in range(m):
    i, j, k = map(int, input().split())
    for a in range(i-1, j):
        ballLi[a] = k

print(*ballLi)