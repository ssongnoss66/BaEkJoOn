# input.txt 파일을 생성하고,입력을 작성해주세요.
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.
import sys

# 이하 입력 코드

trial = int(sys.stdin.readline())

for i in range(trial):
    result = list(sys.stdin.readline().rstrip())
    score = 0
    addScore = 0
    for j in result:
        if j == "O":
            addScore += 1
            score += addScore
        else:
            addScore = 0
    print(score)