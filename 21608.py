import sys

input = sys.stdin.readline

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def solution(one, like):
    map_info = [[[-1, -1] for __ in range(n)] for __ in range(n)]
    max_v = 0

    for i in range(n):
        for j in range(n):
            if classroom[i][j] != -1:
                continue

            v = 0
            w = 0
            for d in range(4):
                nx = j + dx[d]
                ny = i + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if classroom[ny][nx] == -1:
                        w += 1
                    elif classroom[ny][nx] in like:
                        v += 1

            map_info[i][j] = (v, w)
            if max_v < v:
                max_v = v

    desks = []
    for i in range(n):
        for j in range(n):
            if map_info[i][j][0] == max_v:
                desks.append((j, i))

    if len(desks) == 1:
        classroom[desks[0][1]][desks[0][0]] = one
    else:
        emptys = []
        max_w = 0
        for desk in desks:
            x, y = desk
            if max_w < map_info[y][x][1]:
                max_w = map_info[y][x][1]
        for desk in desks:
            x, y = desk
            if map_info[y][x][1] == max_w:
                emptys.append((x, y))
        classroom[emptys[0][1]][emptys[0][0]] = one

    del map_info


n = int(input())
classroom = [[-1] * n for __ in range(n)]
likes = []
for __ in range(n * n):
    likes.append(tuple(map(int, input().split())))

for like in likes[:]:
    solution(like[0], like[1:])

answer = 0
likes.sort()
for i in range(n):
    for j in range(n):
        one = classroom[i][j]
        result = 0
        for d in range(4):
            nx = j + dx[d]
            ny = i + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if classroom[ny][nx] in likes[one - 1][1:]:
                    result += 1
        answer += 0 if result == 0 else 10 ** (result - 1)

print(answer)
