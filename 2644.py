from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
x1, x2 = map(int, input().split())
m = int(input())
graph = [[] for __ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

visited = [False] * n
canFind = False
queue = deque()
queue.append((x1-1, 0))
while queue:
    cur, distance = queue.popleft()
    visited[cur] = True
    
    if cur == x2-1:
        visited[cur] = True
        canFind = True
        break
    
    for next in graph[cur]:
        if not visited[next]:
            queue.append((next, distance+1))

if canFind:
    print(distance)
else:
    print(-1)