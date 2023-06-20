from collections import deque
import sys

input = sys.stdin.readline

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]


def check_condition(curr, next):
    a = maps[curr[1]][curr[0]]
    b = maps[next[1]][next[0]]
    if l <= abs(a - b) <= r:
        return True
    return False


def solution(maps):
    check = False
    visited = [[False] * n for __ in range(n)]
    new_maps = maps[:][:]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            check2 = False
            result = []

            value = 0
            # print(visited)
            queue = deque()
            queue = [(j, i)]
            while queue:
                cx, cy = queue.pop()
                for d in range(4):
                    nx = cx + dx[d]
                    ny = cy + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[ny][nx]:
                            if check_condition((cx, cy), (nx, ny)):
                                check = check2 = True
                                visited[ny][nx] = True
                                queue.append((nx, ny))
                                result.append((nx, ny))

            if check2:
                value = sum(maps[i][j] for j, i in result) // len(result)
                for a, b in result:
                    new_maps[b][a] = value
    maps = new_maps[:][:]
    del new_maps
    if check:
        return True
    return False


n, l, r = map(int, input().split())
maps = [list(map(int, input().split())) for __ in range(n)]

for t in range(2001):
    if not solution(maps):
        print(t)
        break
