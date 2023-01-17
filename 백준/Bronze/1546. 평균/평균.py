# input.txt 파일을 생성하고,입력을 작성해주세요.
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.
import sys

# 이하 입력 코드

subjectNum = int(sys.stdin.readline())
realScore = list(map(int, sys.stdin.readline().split()))

newScorehap = 0

for i in realScore:
    newScorehap += (i / max(realScore) * 100)

print(newScorehap / subjectNum)