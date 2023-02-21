"""4673 셀프 넘버 https://www.acmicpc.net/problem/4673"""

def d(n):                   # n이 12345라 치면
    a = n//10000            # a == 1
    b = (n//1000)%10        # b == 2
    c = (n//100)%10         # c == 3
    d = (n//10)%10          # d == 4
    e = n%10                # e == 5

    return n + a + b + c + d + e

numLi = list(range(1, 10001))     # 1부터 10000까지 리스트
calcLi = []                       # 비워둔 리스트

for num in numLi:                 # 1부터 10000까지 순회    
    calcNum = d(num)              # 1을 d(n)함수에 넣어 계산한 결과값인 d(1)을 calcNum에 할당
    if calcNum <= 10000:          # 계산 결과값이 1만보다 작거나 같아야하니까 if문으로 조건걸고
        calcLi.append(calcNum)    # 1만보다 작으면 비워둔 리스트에 값 추가

printLi = [a for a in numLi if a not in calcLi]
# 리스트 컴프리헨션 활용하여 printLi 생성
# -> 1부터 1만까지 숫자들로 이루어진 numLi의 원소들 중에 계산결과값(셀프넘버)들로 이루어진 calcLi에 없는 원소들로 이루어진 printLi

for j in printLi:
    print(j)

# 숏코딩

# r=range(9999);print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))