# input.txt 파일을 생성하고,입력을 작성해주세요.
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.
import sys

# 이하 입력 코드

testCase = int(sys.stdin.readline())

for i in range(testCase):
    scoreList = list(map(int, sys.stdin.readline().split()))
    studentNum = scoreList[0]
    scoreAverage = (sum(scoreList) - scoreList[0]) / studentNum
    studentAbove = 0
    for j in scoreList:
        if j > scoreAverage:
            studentAbove += 1
    rate = (studentAbove / studentNum * 100)
    print(f"{rate:.3f}%")
    # print("{:.3f}%".format(rate))

# 리스트 범위 지정, 슬라이싱
# round()로 하면 40.000이 출력이 안됨 f-string 활용
