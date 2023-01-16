hap = 0

for i in range(1, 6):
    score = int(input())
    if score >= 40:
        hap += score
    elif score < 40:
        hap += 40
    
print(hap // 5)