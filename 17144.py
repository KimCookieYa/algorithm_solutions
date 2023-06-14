import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dx2 = [1, 0, -1, 0]
dy2 = [0, 1, 0, -1]


def spread(a):
    b = [[0] * c for __ in range(r)]
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                count = 0
                for d in range(4):
                    nx = j + dx[d]
                    ny = i + dy[d]
                    if 0 <= nx < c and 0 <= ny < r:
                        if a[ny][nx] >= 0:
                            count += 1
                            b[ny][nx] += a[i][j] // 5

                a[i][j] = a[i][j] - ((a[i][j] // 5) * count)

    for i in range(r):
        for j in range(c):
            a[i][j] += b[i][j]


def airconditioning(a):
    cur = (0, air_row[0])
    prev_temp = 0
    for d in range(4):
        while True:
            next = (cur[0] + dx[d], cur[1] + dy[d])
            if not (0 <= next[0] < c and 0 <= next[1] < r):
                break
            if a[next[1]][next[0]] == -1:
                break
            temp = a[next[1]][next[0]]
            a[next[1]][next[0]] = prev_temp
            cur = next
            prev_temp = temp

    cur = (0, air_row[1])
    prev_temp = 0
    for d in range(4):
        while True:
            next = (cur[0] + dx2[d], cur[1] + dy2[d])
            if not (0 <= next[0] < c and 0 <= next[1] < r):
                break
            if a[next[1]][next[0]] == -1:
                break
            temp = a[next[1]][next[0]]
            a[next[1]][next[0]] = prev_temp
            cur = next
            prev_temp = temp


r, c, t = map(int, input().split())
a = []
air_row = []
for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)
    if row[0] == -1:
        air_row.append(i)

for __ in range(t):
    spread(a)
    airconditioning(a)

answer = 2
for i in range(r):
    answer += sum(a[i])
print(answer)
