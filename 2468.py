import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def solution(n):
    def print_visited():
        for i in range(n):
            print(visited[i])
        print('')
    
    def bfs(k, px, py):
        queue = [([px, py])]
        
        while queue:
            cx, cy = queue.pop()
            visited[cy][cx] = True
            
            for i in range(4):
                nx = cx + dir[i][0]
                ny = cy + dir[i][1]
                
                if 0 <= nx and nx < n and 0 <= ny and ny < n:
                    if not visited[ny][nx] and a[ny][nx] >= k:
                        queue.append((nx, ny))
      
    answer = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    min_val = min(map(min, a))
    max_val = max(map(max, a))
    for k in range(min_val, max_val+1):
        sum_val = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and a[i][j] >= k:
                    bfs(k, j, i)
                    sum_val += 1
        
        answer = max(answer, sum_val)
        
        visited = [[False for _ in range(n)] for _ in range(n)]
    
    return answer

answer = solution(n)
print(answer)