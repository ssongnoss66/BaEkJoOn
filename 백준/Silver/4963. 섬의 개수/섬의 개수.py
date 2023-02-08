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
# 해결책 ; 소스 1의 최대 재귀 깊이를 1,000,000 정도로 크게 설정하면 런타임 에러 없이 실행