n = int(input())
resultLi = list(map(int, input().split()))
score = 0
howMany = 0

for i in resultLi:
    if i == 1:
        score += 1
        howMany += 1
        if howMany > 1:
            score += (howMany - 1)
    elif i == 0:
        howMany = 0
        
print(score)