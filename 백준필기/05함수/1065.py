"""1065 한수 https://www.acmicpc.net/problem/1065"""

def hansu(num):
    cnt = 99
    numB = 100
    if num < 100:
        return(num)
    else:
        while True:
            if (numB//100) - ((numB % 100) // 10) == ((numB % 100) // 10) - ((numB % 100) % 10):
                cnt += 1
            if numB == num:
                break
            numB += 1
        return(cnt)
                
N = int(input())
print(hansu(N))