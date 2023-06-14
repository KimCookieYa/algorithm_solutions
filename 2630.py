import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
color = [0, 0]

def solution(a):
    def solution(a, start, end, n):
        current_color = a[start[1]][start[0]]
        if n == 1:
            color[current_color] += 1
            return
        
        for i in range(start[1], end[1]+1):
            for j in range(start[0], end[0]+1):
                if a[i][j] != current_color:
                    solution(a, start, [end[0]-n//2, end[1]-n//2], n//2)
                    solution(a, [start[0]+n//2, start[1]], [end[0], end[1]-n//2], n//2)
                    solution(a, [start[0], start[1]+n//2], [end[0]-n//2, end[1]], n//2)
                    solution(a, [start[0]+n//2, start[1]+n//2], end, n//2)
                    return
        
        color[current_color] += 1
    
    n = len(a[0])
    solution(a, [0, 0], [n-1, n-1], n)

solution(a)
print(color[0])
print(color[1])