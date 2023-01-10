trial = int(input())
for i in range(1, trial+1):
    numList = list(map(int, input().split()))
    print(f"#{i} {round(sum(numList)/len(numList))}")