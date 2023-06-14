from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

tomatos = [[[] for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        tomatos[i][j] = list(map(int, input().split()))
direction = [[1, 0, 0],
             [-1, 0, 0],
             [0, 1, 0],
             [0, -1, 0],
             [0, 0, 1],
             [0, 0, -1]]
day = 0
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 1:
                queue.append((i, j, k))

while True:
    nextQueue = deque()
    isRiped = False
    while queue:
        curZ, curY, curX = queue.popleft()
        visited[curZ][curY][curX] = True
        
        for mz, my, mx in direction:
            nextZ = curZ + mz
            nextY = curY + my
            nextX = curX + mx
            if 0 <= nextZ and nextZ < h and 0 <= nextY and nextY < n and 0 <= nextX and nextX < m:
                if not visited[nextZ][nextY][nextX]:
                    visited[nextZ][nextY][nextX] = True
                    if tomatos[nextZ][nextY][nextX] == 0:
                        tomatos[nextZ][nextY][nextX] = 1
                        nextQueue.append((nextZ, nextY, nextX))
                        isRiped = True
    
    if not isRiped:
        break
    
    queue = nextQueue
    del nextQueue
    day += 1

for floor in tomatos:
    for row in floor:
        if 0 in row:
            day = -1
            break
    else:
        continue
    break

print(day)