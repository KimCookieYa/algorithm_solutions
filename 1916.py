from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
dp = [INF] * n
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges[a-1].append((cost, b-1))
a, b = map(int, input().split())

dp[a-1] = 0
queue = [(0, a-1)]
while queue:
    curCost, cur = heappop(queue)
    
    if dp[cur] < curCost:
        continue
    
    for nextCost, next in edges[cur]:
        newCost = curCost+nextCost
        if dp[next] > newCost:
            dp[next] = newCost
            heappush(queue, (newCost, next))

print(dp[b-1])