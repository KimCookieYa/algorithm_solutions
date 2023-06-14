from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

tomatos = [[] for _ in range(n)]
for j in range(n):
    tomatos[j] = list(map(int, input().split()))
direction = [[1, 0],
             [-1, 0],
             [0, 1],
             [0, -1]]
day = 0
visited = [[False] * m for _ in range(n)]

queue = deque()
for j in range(n):
    for k in range(m):
        if tomatos[j][k] == 1:
            queue.append((j, k))

while True:
    nextQueue = deque()
    isRiped = False
    while queue:
        curY, curX = queue.popleft()
        visited[curY][curX] = True
        
        for my, mx in direction:
            nextY = curY + my
            nextX = curX + mx
            if 0 <= nextY and nextY < n and 0 <= nextX and nextX < m:
                if not visited[nextY][nextX]:
                    visited[nextY][nextX] = True
                    if tomatos[nextY][nextX] == 0:
                        tomatos[nextY][nextX] = 1
                        nextQueue.append((nextY, nextX))
                        isRiped = True
    
    if not isRiped:
        break
    
    queue = nextQueue
    del nextQueue
    day += 1

for row in tomatos:
    if 0 in row:
        day = -1
        break

print(day)