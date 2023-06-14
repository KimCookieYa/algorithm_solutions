import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
todo = [[0, '']] * l
for i in range(l):
    sec, dir = input().split()
    todo[i] = [int(sec), 1 if dir == 'L' else -1]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
direction = 0

queue = [[1, 1]]
tIdx = 0
for t in range(1, 10000+n):
    head = queue[-1]
    nextHead = [head[0]+dy[direction], head[1]+dx[direction]]
    
    if (not ((0 < nextHead[0] and nextHead[0] <= n) and (0 < nextHead[1] and nextHead[1] <= n))) or (nextHead in queue):
        print(t)
        break
    
    queue.append(nextHead)
    if nextHead in apple:
        apple.remove(nextHead)
    else:
        queue.pop(0)
    
    if tIdx < l:
        if t == todo[tIdx][0]:
            direction += todo[tIdx][1]
            if direction < 0:
                direction = 3
            elif direction > 3:
                direction = 0
            tIdx += 1