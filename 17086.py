from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    visited = [[False] * m for __ in range(n)]
    queue = deque()
    queue.append((x, y, 1))
    visited[y][x] = True
    while queue:
        cur_x, cur_y, depth = queue.popleft()
        
        for k in range(8):
            next_x = cur_x + dx[k]
            next_y = cur_y + dy[k]
            
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if sea[next_y][next_x] == 1:
                continue
            
            if not visited[next_y][next_x]:
                queue.append((next_x, next_y, depth+1))
                distance[next_y][next_x] = min(distance[next_y][next_x], sea[y][x] + depth-1)
                visited[next_y][next_x] = True
            
                
    
    del queue

n, m = map(int, input().split())
sharks = []
sea = [list(map(int, input().split())) for __ in range(n)]

distance = [[1000000] * m for __ in range(n)]
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

for i in range(n):
    for j in range(m):
        if sea[i][j] == 1:
            bfs(j, i)

answer = 0
for i in range(n):
    for j in range(m):
        if distance[i][j] != 1000000:
            answer = max(answer, distance[i][j])

print(answer)