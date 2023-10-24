import sys

input = sys.stdin.readline

n = 9
a = [list(map(int, input().split())) for __ in range(n)]

answer = [0, 0, 0]
for i in range(n):
    for j in range(n):
        if a[i][j] > answer[0]:
            answer = [a[i][j], i, j]

print(answer[0])
print(answer[1] + 1, answer[2] + 1)
