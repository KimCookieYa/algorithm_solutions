# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

mx = [-1, -1, -1, 0, 0, 1, 1, 1]
my = [-1, 0, 1, -1, 1, -1, 0, 1]


def calculate(c):
    if c == s:
        return 0
    p, cy, cx = c
    result = 0
    if maps[cy][cx] == "P":
        result = -3
    for i in range(8):
        nx = cx + mx[i]
        ny = cy + my[i]
        if 0 <= nx < h and 0 <= ny < w:
            if maps[ny][nx] == "P":
                result += 1
    return result


w, h = map(int, input().split())

ps = []
maps = [[0]] * w
for i in range(w):
    temp = input().strip()
    if "S" in temp:
        j = temp.index("S")
        s = (2, i, j)
    if "E" in temp:
        e = (0, i, temp.index("E"))
    if "P" in temp:
        for j in range(h):
            if temp[j] == "P":
                ps.append((1, i, j))
    maps[i] = temp

visited = [[False] * h for __ in range(w)]
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

queue = []
heappush(queue, s)
visited[s[1]][s[2]] = True
score = 0
while queue:
    # while not queue.empty():
    # 	queue.get()
    c = heappop(queue)
    if c == e:
        break
    score += calculate(c)
    cx = c[2]
    cy = c[1]

    for d in range(4):
        nx = cx + dx[d]
        ny = cy + dy[d]
        if 0 <= nx < h and 0 <= ny < w:
            if not visited[ny][nx]:
                if (0, ny, nx) == e:
                    heappush(queue, e)
                elif (1, ny, nx) in ps:
                    heappush(queue, (1, ny, nx))
                else:
                    heappush(queue, (2, ny, nx))
                visited[ny][nx] = True

print(max(score, 0))
