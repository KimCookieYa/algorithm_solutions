from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    edges[a-1].append(b-1)

visited = [False] * n
queue = deque()
queue.append((x-1, 0))
visited[x-1] = -1
while queue:
    cur, distance = queue.popleft()
    for next in edges[cur]:
        if visited[next] == False:
            visited[next] = distance+1
            queue.append((next, distance+1))

if k not in visited:
    print(-1)
else:
    for i in range(n):
        if visited[i] == k:
            print(i+1)