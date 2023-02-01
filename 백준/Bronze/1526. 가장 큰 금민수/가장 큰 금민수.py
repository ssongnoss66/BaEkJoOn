"""1526 가장 큰 금민수 https://www.acmicpc.net/problem/1526"""

# 4와 7로만 이루어진 리스트 중 가장 작은값은 4니까 시작값 strt에 4 할당해두고 시작
strt = 4

# strt에 1씩 추가하면서 while문 돌 때 중복 여부와 관계 없이 4와 7로만 이루어지면 되니까 세트 활용
strtSt = set(str(strt).strip())
idx = -1

# 4와 7로만 이루어진 리스트 채우기 위해 numLi 비워두기
numLi = []

inpt = int(input())

while True:
    # 세트가 4 / 7 / 4 7 중에 하나면 (현재 strt 4 ; 세트에 4만 들어있음)
    if strtSt == {"4"} or strtSt == {"7"} or strtSt == {"4", "7"}:
        # 리스트에 추가
        numLi.append(strt)
        idx += 1
    # strt에 1씩 추가
    strt += 1
    # strt 값이 1 추가되면서 바꼈으니까 세트도 새로 할당해야됨
    strtSt = set(str(strt).strip())
    # 리스트에서 가장 큰 값 (가장 최근에 추가된 값)이 입력받은 값보다 크면 (입력값보다 작거나 같은 값을 출력해야되니까)
    if numLi[idx] > inpt:
        # while문 종료
        break

print(numLi[idx-1])