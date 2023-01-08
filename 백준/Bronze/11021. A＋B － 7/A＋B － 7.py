import sys
input = sys.stdin.readline

trial = int(input())

for i in range(0, trial):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a+b}")