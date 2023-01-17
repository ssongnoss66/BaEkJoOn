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

# 간단하게...ㅠㅠ