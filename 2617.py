import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = True

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = True

answer = 0
for i in range(n):
    if graph[i].count(True) > n//2:
        answer += 1
    col = [graph[j][i] for j in range(n)]
    if col.count(True) > n//2:
        answer += 1

print(answer)