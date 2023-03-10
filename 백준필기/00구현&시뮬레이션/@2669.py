"""2669 직사각형 네개의 합집합의 면적 구하기 https://www.acmicpc.net/problem/2669"""

# internetVer

paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    #사각형 부분만 1로 바꾸어줌
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

answer = 0
for row in paper:
    answer += sum(row)
print(answer)

"""틀렸다... 이러면 떨어져 있을 때 게산이 안됨
sqDict = {}

for i in range(4):
    a, b, c, d = map(int, input().split())                      # 1 2 4 4
    for j in range(b, d+1):
        for k in range(a, c+1):
            try:
                sqDict[k].add(j)
            except:
                sqDict[k] = set()
                sqDict[k].add(j)

print(sqDict)

strt = 1
prntHap = 0

while True:
    try:
        if strt > max(sqDict.keys()):
            break
        print(f"가로 좌표 시작이 {strt}일 때 세로변 길이는 {(max(sqDict[strt] & sqDict[strt + 1])) - (min(sqDict[strt] & sqDict[strt + 1]))}")
        prntHap += (max(sqDict[strt] & sqDict[strt + 1])) - (min(sqDict[strt] & sqDict[strt + 1]))
        strt += 1
    except:
        if strt > max(sqDict.keys()):
            print(f"strt가 {strt}로 max값 {max(sqDict.keys())}보다 커서 순회 끝")
            break
        strt += 1

print(prntHap)
"""