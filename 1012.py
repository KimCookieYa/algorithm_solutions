from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for k in range(4):
            next_x = cur_x + dx[k]
            next_y = cur_y + dy[k]
            
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            
            if graph[next_y][next_x]:
                queue.append((next_x, next_y))
                graph[next_y][next_x] = 0

t = int(input())
while t > 0:
    m, n, k = map(int, input().split())
    graph = [[0] * m for __ in range(n)]
    for __ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(j, i)
                answer += 1
    
    print(answer)
    t -= 1