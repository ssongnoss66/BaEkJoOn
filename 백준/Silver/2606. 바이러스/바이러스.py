"""2606 바이러스 https://www.acmicpc.net/problem/2606"""

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n+1)

def dfs(start):
    stack = [start]
    visited[start] = True
    total = 0
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                total += 1
                stack.append(adj)
    return total

print(dfs(1))