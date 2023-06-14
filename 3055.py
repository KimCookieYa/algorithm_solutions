from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
maps = [[] * c for _ in range(r)]
waterQueue = deque()
HedgehogQueue = deque()
for i in range(r):
    row = list(input().rstrip())
    maps[i] = row
    if '*' in row:
        waterQueue.append((row.index('*'), i))
    if 'S' in row:
        idx = row.index('S')
        HedgehogQueue.append((idx, i))
        maps[i][idx] = 0
    
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 1000000
time = 0
while True:
    nextwaterQueue = deque()
    while waterQueue:
        curX, curY = waterQueue.popleft()
        
        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX and nextX < c and 0 <= nextY and nextY < r:
                if maps[nextY][nextX] == '.':
                    maps[nextY][nextX] = '*'
                    nextwaterQueue.append((nextX, nextY))
    
    waterQueue = nextwaterQueue
    del nextwaterQueue
    
    isMoved = False
    nextQueue = deque()
    while HedgehogQueue:
        curX, curY = HedgehogQueue.popleft()
        
        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX and nextX < c and 0 <= nextY and nextY < r:
                if maps[nextY][nextX] == '.':
                    maps[nextY][nextX] = maps[curY][curX] + 1
                    nextQueue.append((nextX, nextY))
                    isMoved = True
                elif maps[nextY][nextX] == 'D':
                    answer = min(answer, maps[curY][curX] + 1)
                    isMoved = True
    
    HedgehogQueue = nextQueue
    del nextQueue

    if not isMoved:
        break
    
    time += 1

if answer == 1000000:
    print("KAKTUS")
else:
    print(answer)