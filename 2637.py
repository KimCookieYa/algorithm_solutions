import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [[] for __ in range(n+1)]
for __ in range(m):
    x, y, k = map(int, input().split())
    edges[x].append((y, k))

dp = [[] * n for __ in range(n+1)]
for i in range(1, n):
    if not edges[i]:
        dp[i] = [0] * n
        dp[i][i] = 1

def dfs(cur):
    if dp[cur]:
        return dp[cur]

    temp = [0 for __ in range(n)]
    for next, next_cnt in edges[cur]:
        required_items = dfs(next)
        for i in range(n):
            if required_items[i] > 0:
                temp[i] += next_cnt * required_items[i]
    
    dp[cur] = temp
    return dp[cur]

answer = dfs(n)
for i in range(1, n):
    if answer[i] > 0:
        print(i, answer[i])