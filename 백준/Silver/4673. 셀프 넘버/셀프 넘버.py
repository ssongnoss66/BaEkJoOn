def d(n):
    a = n//10000
    b = (n//1000)%10
    c = (n//100)%10
    d = (n//10)%10
    e = n%10

    return n + a + b + c + d + e

numLi = list(range(1, 10001))
calcLi = []

for i in numLi:
    c = d(i)
    if c <= 10000:
        calcLi.append(c)

printLi = [a for a in numLi if a not in calcLi]

for j in printLi:
    print(j)