howMany = int(input())

for i in range(1,howMany+1):
    print(sum(list(map(int, input().split()))))
    i += 1