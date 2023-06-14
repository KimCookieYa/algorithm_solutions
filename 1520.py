import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for __ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dp = [[-1] * n for __ in range(m)]

def solution(x, y):
    if (x, y) == (n-1, m-1):
        return 1
    
    if dp[y][x] == -1:
        dp[y][x] = 0
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[y][x] > maps[ny][nx]:
                    dp[y][x] += solution(nx, ny)
    
    return dp[y][x]

print(solution(0, 0))