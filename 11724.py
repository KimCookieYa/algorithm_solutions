from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def bfs(start):
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for next in edges[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

edges = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
queue = deque()
visited = [False] * (n+1)
answer = 0
for node in range(1, n+1):
    if not visited[node]:
        bfs(node)
        answer += 1

print(answer)