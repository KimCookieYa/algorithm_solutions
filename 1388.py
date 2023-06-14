from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]
def dfs(shape, cur_x, cur_y):
    if shape == '-':
        next_x = cur_x + dx[0]
        next_y = cur_y + dy[0]
        
        if 0 <= next_y < n and 0 <= next_x < m:
            if visited[next_y][next_x]:
                return
            if shape == floors[next_y][next_x]:
                visited[next_y][next_x] = True
                dfs(shape, next_x, next_y)
    elif shape == '|':
        next_x = cur_x + dx[1]
        next_y = cur_y + dy[1]
        
        if 0 <= next_y < n and 0 <= next_x < m:
            if visited[next_y][next_x]:
                return
            if shape == floors[next_y][next_x]:
                visited[next_y][next_x] = True
                dfs(shape, next_x, next_y)


n, m = map(int, input().split())
floors = [input().rstrip() for __ in range(n)]
visited = [[False] * m for __ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(floors[i][j], j, i)
            answer += 1

print(answer)