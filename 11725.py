import sys
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

answer = [1] * n
visited = [False] * n
stack = [0]
while stack:
    cur = stack.pop()
    for next in edges[cur]:
        if not visited[next]:
            stack.append(next)
            answer[next] = cur+1
            visited[next] = True

for i in answer[1:]:
    print(i)