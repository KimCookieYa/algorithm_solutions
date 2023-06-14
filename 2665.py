from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
rooms = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

heap = []
heappush(heap, [0, 0, 0])
visited[0][0] = 1

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

while heap:
    a, x, y = heappop(heap)
    if x == n - 1 and y == n - 1:
        print(a)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            if rooms[nx][ny] == 0:
                heappush(heap, [a + 1, nx, ny])
            else:
                heappush(heap, [a, nx, ny])