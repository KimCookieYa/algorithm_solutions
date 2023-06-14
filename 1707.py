import sys
input = sys.stdin.readline

t = int(input())
while t > 0:
    v, e = map(int, input().split())
    edges = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    
    colors = [0] * v
    check = False
    for i in range(v):
        if colors[i] == 0:
            queue = [i]
            colors[i] = 1
            while queue:
                cur = queue.pop(0)
                color = colors[cur]
                for next in edges[cur]:
                    if colors[next] == 0:
                        queue.append(next)
                        colors[next] = -color
                    elif colors[next] == color:
                        check = True
        if check:
            break                 
    
    if check:
        print("NO")
    else:
        print("YES")
    
    t -= 1