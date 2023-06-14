import sys
input = sys.stdin.readline

n = int(input())
maps = [list(input().rstrip()) for __ in range(n)]
visited = [[False] * n for __ in range(n)]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def dfs(num, cur_x, cur_y):
    for k in range(4):
        next_x = cur_x + dx[k]
        next_y = cur_y + dy[k]
        
        if 0 <= next_y < n and 0 <= next_x < n:
            if visited[next_y][next_x]:
                continue
            if maps[next_y][next_x] == '1':
                visited[next_y][next_x] = True
                maps[next_y][next_x] = num
                dfs(num, next_x, next_y)

num = '1'
answers = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == '1':
            visited[i][j] = True
            maps[i][j] = num
            dfs(num, j, i)
            num = str(int(num)+1)

answer = [0] * int(num)
for i in range(n):
    for j in range(n):
        answer[int(maps[i][j])] += 1

answer = answer[1:]
answer.sort()
print(len(answer))
for a in answer:
    print(a)