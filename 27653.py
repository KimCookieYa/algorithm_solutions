from collections import deque
import sys
input = sys.stdin.readline

def find_parent(x):
    if x != parents[x]:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    px = find_parent(x)
    py = find_parent(y)
    if px < py:
        parents[y] = px
    else:
        parents[x] = py


n = int(input())
a = list(map(int, input().split()))
parents = [i for i in range(n+1)]
edges = [[] for __ in range(n+1)]
for __ in range(n-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
    union_parent(u, v)

answer = 0
weights = [0] * (n+1)
queue = deque()
queue.append((parents[1], 0))
visited = [False] * (n+1)
while queue:
    cur_node, cur_count = queue.popleft()
    visited[cur_node] = True
    
    if cur_count < a[cur_node-1]:
        answer += a[cur_node-1]-cur_count
        cur_count = a[cur_node-1]
        
    for next_node in edges[cur_node]:
        if not visited[next_node]:
            queue.append((next_node, cur_count))

print(answer)