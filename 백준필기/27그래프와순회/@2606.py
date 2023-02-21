"""2606 바이러스 https://www.acmicpc.net/problem/2606"""

comp = int(input())
ntwrk = int(input())

arr = [[] for _ in range(comp+1)]

for _ in range(ntwrk):
    m, n = map(int, input().split())
    arr[m].append(n)
    arr[n].append(m)                                # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

def dfs(start):                                     # start 1
    visited = [[False] for _ in range(comp+1)]      # vstd [F F F F F F F F]
    visited[start] = True                           # vstd [F T F F F F F F]
    stack = [start]                                 # stck [1]
    total = 0
    while stack:
        cur = stack.pop()                           # cur 1 stck [] / cur 5 stck [2] // cur 6 stck [2] /// cur 2 stck [] //// cur 3 stck [] !!끝!!
        for adj in arr[cur]:                        # arr[1]은 [2, 5] / arr[5]는 [1, 2, 6] // arr[6]은 [5] ; visited[5]는 방문한 적 있으니까 /// arr[2]는 [1, 3, 5] //// arr[3]은 [2] ; visited[2]는 이미 방문한 적 있으니까
            if not visited[adj]:
                visited[adj] = True                 # vstd [F T T F F T F F] / vstd [F T T F F T T F] /// vstd [F T T T F T T F]
                total += 1                          # ttl 2 / ttl 3 /// ttl 4
                stack.append(adj)                   # stck [2, 5] / stck [2, 6] /// stck [3]
    return total

print(dfs(1))

"""teacher Ver
comp = int(input())                         # 7
ntwrk = int(input())                        # 6

graph = [[] for _ in range(comp + 1)]

for tc in range(ntwrk):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)                    # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

visited = [False] * (comp + 1)              # [[False],[False],[False],[False],[False],[False],[False],[False]]

def dfs(start):                             # 0은 비어있으니까 1로 시작 dfs(1)
    stack = [start]                         # stack = [1] 돌아갈 곳 기록?!?!뭔솔!!!
    visited[start] = True                   # visited[1] = True ; 1에서 출발하니까 일단 여기는 방문 처리 [[False],[True],[False],[False],[False],[False],[False],[False]]
    total = 0           
    while stack:                            # 1️⃣ 스택 비면 while문 멈춰 2️⃣ 돌아 3️⃣ 돌아 4️⃣ 스택에 2 있으니까 돌아 5️⃣ 돌아 🔴 stack 비어있으니까 고만 돌아!
        cur = stack.pop()                   # 1️⃣ cur 1 stack [] 2️⃣ cur 5 stack [2] 3️⃣ cur 6 stack [2] 4️⃣ cur 2 stack [] 5️⃣ cur 3 stack []
        for adj in graph[cur]:              # 1️⃣ graph[1]은 [2, 5] 2️⃣ graph[5]는 [1, 2, 6] 3️⃣ graph[6]은 [5]; visited[5]는 이미 방문해서 True임! 4️⃣ graph[2]는 [1, 3, 5] 5️⃣ graph[3]은 [2]; visited[2]는 이미 방문해서 True!
            if not visited[adj]:            
                visited[adj] = True         # 1️⃣ [F F T F F T F F] 2️⃣ [F F T F F T T F] 4️⃣ [F F T T F T T F]
                total += 1                  # 1️⃣ total 2 2️⃣ total 3 4️⃣ total 4
                stack.append(adj)           # 1️⃣ stack [2, 5] 2️⃣ stack [2, 6] 4️⃣ stack [3]
    return total

print(dfs(1))
"""