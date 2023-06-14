from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

queue = deque()
queue.append(0)
visited = [False] * n
while queue:
    curNode = queue.popleft()
    visited[curNode] = True
    
    for nextNode in edges[curNode]:
        if not visited[nextNode]:
            queue.append(nextNode)

answer = len(list(filter(lambda x: x == True, visited))) - 1
print(answer)