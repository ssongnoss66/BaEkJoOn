"""4344 평균은 넘겠지 https://www.acmicpc.net/problem/4344"""

cnt = 0

for i in range(int(input())):
    cnt = 0
    numLi = list(map(int, input().split()))
    studNum = numLi[0]
    total = sum(numLi) - studNum
    aver = total / studNum
    for j in range(1, studNum+1):
        if numLi[j] > aver:
            cnt += 1
    print("{:.3f}%".format(cnt/studNum*100))

# f-string 출력 ; 소수점 셋째자리까지 출력