"""4963 섬의 개수 https://www.acmicpc.net/problem/4963"""

# bfs 풀어보기

# dfs

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
  dx = [0, 0, 1, 1, 1, -1, -1, -1]
  dy = [1, -1, 1, 0, -1, 1, 0, -1]

  arr[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
      dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if w == h == 0:
    break
  arr = [list(map(int, input().split())) for _ in range(h)]
  cnt = 0

  for i in range(h):
    for j in range(w):
      if arr[i][j] == 1:
        dfs(i, j)
        cnt += 1
  print(cnt)

# RecursionError는 재귀와 관련된 에러! 가장 많이 발생하는 이유는 Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때 발생
# 해결책1 ; 재귀 함수 사용하지 않기 / DFS 말고 BFS 사용하거나 반복문으로 구현하기
# 해결책2 ; 소스 1의 최대 재귀 깊이를 1,000,000 정도로 크게 설정하면 런타임 에러 없이 실행
# 이차원 리스트에서 좌표로 호출할 때 리스트[행][열]

""" internetVer

# dfs

from pprint import pprint

def dfs(x, y):                                                      # 델타탐색부터 설정
  dx = [1, 1, -1, -1, 1, -1, 0, 0]                                  # 오 오아래 왼 왼아래 오위 왼위 아래 위
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  field[x][y] = 0                                                   # (x, y) 좌표 자리를 1에서 0으로 터뜨려서 이후에는 이 자리 안 돌게 함
  for i in range(8):                                                # 상하좌우+네모서리 ; 8번 돌아야됨
    nx = x + dx[i]                                                  # x(y)에 dx(dy) 리스트의 인덱스 i에 해당하는 값을 더함
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:          # 더한 값이 0보다 크거나 같고 너비(높이)보다 작으며! & 더한 값에 해당하는 좌표를 가진 자리가 1이면
      dfs(nx, ny)                                                   # 그 자리에서 또 이 함수 반복 ; 인접한 1 다 터뜨려서 더이상 인접한 1 없을 때까지!

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  field = []                                                        # 리스트 비워두기
  count = 0                                                         # 섬 갯수 카운트할 변수 비워두기
  for _ in range(h):
    field.append(list(map(int, input().split())))                   # 리스트 채워서 행렬 만들기
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        dfs(i, j)
        count += 1
  
  print(count)


# bfs

from collections import deque
import sys
read = sys.stdin.readline

def bfs(x, y):
  dx = [1, -1, 0, 0, 1, -1, 1, -1]
  dy = [0, 0, -1, 1, -1, 1, 1, -1]
  field[x][y] = 0
  q = deque()
  q.append([x, y])
  while q:
    a, b = q.popleft()
    for i in range(8):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
        field[nx][ny] = 0
        q.append([nx, ny])

while True:
  w, h = map(int, read().split())
  if w == 0 and h == 0:
    break
  field = []
  count = 0
  for _ in range(h):
    field.append(list(map(int, read().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        bfs(i, j)
        count += 1
  print(count)
"""