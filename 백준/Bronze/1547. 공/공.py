import sys
inpt = sys.stdin.readline

ballLi = [0, 1, 1]

for _ in range(int(inpt())):
    x, y = map(int, inpt().split())
    ballLi[x - 1], ballLi[y - 1] = ballLi[y - 1], ballLi[x - 1]

print(ballLi.index(0) + 1)