from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
def bfs(S, X, Y):
    virus = deque(viruss)
    cnt = 0
    while virus:
        if cnt == S:
            break
        for __ in range(len(virus)):
            cur_no, cur_x, cur_y = virus.popleft()
            for k in range(4):
                next_x = cur_x + dx[k]
                next_y = cur_y + dy[k]
                
                if 0 <= next_y < n and 0 <= next_x < n:
                    if maps[next_y][next_x] == 0:
                        maps[next_y][next_x] = cur_no
                        virus.append((maps[next_y][next_x], next_x, next_y))
        cnt += 1
    
    return maps[X][Y]


n, k = map(int, input().split())
maps = [[0] * n for __ in range(n)]
viruss = []
for i in range(n):
    maps[i] = list(map(int, input().split()))
    for j in range(n):
        if maps[i][j] != 0:
            viruss.append((maps[i][j], j, i))

visited = [[False] * n for __ in range(n)]
s, x, y = map(int, input().split())

viruss.sort()
print(bfs(s, x-1, y-1))