from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
out_node = [[] for _ in range(n)] 
in_degree = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    in_degree[b-1] += 1
    out_node[a-1].append(b-1)

visited = [False] * n
queue = deque()
answer = []

for i in range(n):
    if in_degree[i] == 0:
        queue.append(i)
        visited[i] = True

while queue:
    cur = queue.popleft()
    answer.append(cur+1)
    
    for out in out_node[cur]:
        if not visited[out]:
            in_degree[out] -= 1
            
            if in_degree[out] == 0:
                queue.append(out)
                visited[out] = True

print(*answer)