import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def dfs(cur):
    global result
    result += 1
    x, y = cur
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[ny][nx] and (nx, ny) in trashs:
                visited[ny][nx] = True
                dfs((nx, ny))


n, m, k = map(int, input().split())
trashs = []
for __ in range(k):
    r, c = map(int, input().split())
    trashs.append((c - 1, r - 1))

answer = 0
visited = [[False] * m for __ in range(n)]
for trash in trashs:
    cx, cy = trash
    if not visited[cy][cx]:
        visited[cy][cx] = True
        result = 0
        dfs(trash)
        answer = max(answer, result)

print(answer)
