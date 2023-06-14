import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for __ in range(m):
    x, y = map(int, input().split())
    union(parent, x, y)

costs = [list(map(int, input().split())) for __ in range(n)]
edges = []
result = 0
for i in range(n):
    for j in range(n):
        if i < j and find(parent, i+1) != find(parent, j+1):
            edges.append((costs[i][j], j, i))

edges.sort()
answers = []
for edge in edges:
    cost, a, b = edge
    if a == 0 or b == 0:
        continue
    if find(parent, a+1) != find(parent, b+1):
        union(parent, a+1, b+1)
        result += cost
        answers.append((a+1, b+1))

print(result, len(answers))
for answer in answers:
    print(*answer)