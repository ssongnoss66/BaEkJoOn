# input.txt 파일을 생성하고,입력을 작성해주세요.
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.
import sys

# 이하 입력 코드

studentList = list(range(1, 31))
notList = []
yesList = []

for i in range(28):
    studentId = int(input())
    yesList.append(studentId)

for j in studentList:
    if not j in yesList:
        notList.append(j)
    
print(sorted(notList)[0])
print(sorted(notList)[1])