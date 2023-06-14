import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(cur, cnt):
    visited[cur] = True
    
    for next in edges[cur]:
        if isInside[next] == '1':
            cnt += 1
        elif not visited[next]:
            cnt = dfs(next, cnt)
    
    return cnt

n = int(input())
isInside = input()

visited = [False] * n
answer = 0
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
    if isInside[a-1] == '1' and isInside[b-1] == '1':
        answer += 2

for cur in range(n):
    if isInside[cur] == '1' or visited[cur]:
        continue
    
    temp = dfs(cur, 0)
    answer += temp * (temp-1)

print(answer)