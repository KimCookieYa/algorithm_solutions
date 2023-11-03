n = int(input())
k = 100
arr = [list(map(int, input().split())) for __ in range(n)]
paper = [[False for __ in range(k)] for __ in range(k)]

answer = 0
for a in arr:
    sx = a[0] - 1
    sy = a[1] - 1
    for i in range(sy, sy + 10):
        for j in range(sx, sx + 10):
            if not paper[i][j]:
                paper[i][j] = True
                answer += 1

print(answer)
