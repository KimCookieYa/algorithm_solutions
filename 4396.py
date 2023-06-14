import sys
input = sys.stdin.readline

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [0, -1, 1, 1, -1, 0, 1, -1]

def count_bomb(x, y):
    global is_bombed
    if maps[y][x] == '*':
        is_bombed = True
        return
    
    count = 0
    for d in range(len(dx)):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[ny][nx] == '*':
                count += 1
    
    answer[y][x] = str(count)
        

n = int(input())
maps = [input().strip() for __ in range(n)]
opend = [input().strip() for __ in range(n)]
is_bombed = False

answer = [['.'] * n for __ in range(n)]

for i in range(n):
    for j in range(n):
        if opend[i][j] == 'x':
            count_bomb(j, i)

if is_bombed:
    for i in range(n):
        for j in range(n):
            if maps[i][j] == '*':
                answer[i][j] = '*'

for i in range(n):
    print(''.join(answer[i]))