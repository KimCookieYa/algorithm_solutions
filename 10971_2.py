import sys
n = int(input())
city = [[]] * n
for i in range(n):
    city[i] = list(map(int, sys.stdin.readline().split()))
visited = [False] * n
answer = 1e9

def dfs(cur, dist, cost):
    global answer
    
    if dist == n:
        if city[cur][0] > 0:
            answer = min(answer, cost + city[cur][0])
        return

    for next_cur in range(1, n):
        if city[cur][next_cur] > 0 and not visited[next_cur]:
            visited[next_cur] = True
            dfs(next_cur, dist+1, cost + city[cur][next_cur])
            visited[next_cur] = False

dfs(0, 1, 0)
print(answer)