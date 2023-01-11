num = int(input())
hap = 0

while num > 0:
    hap += (num % 10)
    num = num//10

print(hap)