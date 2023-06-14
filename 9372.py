from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    n, m = map(int, input().split())
    edges = [[] for __ in range(n)]
    for __ in range(m):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    
    visited = [False] * n
    answer = 0
    queue = deque()
    queue.append(0)
    visited[0] = True
    while queue:
        cur = queue.popleft()
        
        for next in edges[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                answer += 1
    
    print(answer)