t = int(input())

for i in range(t):
    n = int(input())
    print(sum(i for i in map(int, input().split())))