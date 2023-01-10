trial = int(input())
for i in range(1, trial+1):
    a, b = map(int, input().split())
    print(f"#{i} {a//b} {a%b}")