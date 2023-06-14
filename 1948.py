import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
m = int(input())

citys = [[] for __ in range(n)]
for __ in range(m):
    start, end, cost = map(int, input().split())
    citys[start-1].append((cost, end-1))

start, end = map(int, input().split())
dp = [0] * n
back_path = [[] for __ in range(n)]

def dfs(cur_node, hour):
    if cur_node == end-1:
        return
    
    for next_cost, next_node in citys[cur_node]:
        if dp[next_node] < hour+next_cost:
            back_path[next_node] = [cur_node]
            dp[next_node] = hour+next_cost
            
            dfs(next_node,  hour+next_cost)
        elif dp[next_node] == hour+next_cost:
            back_path[next_node].append(cur_node)

def count_city(cur):
    global answer
    if cur == start-1:
        return
    for next in back_path[cur]:
        if (cur, next) not in visited:
            answer += 1
            visited.append((cur, next))
            count_city(next)

dfs(start-1, 0)
print(dp[end-1])
answer = 0
visited = []
count_city(end-1)
print(answer)