import sys

input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for __ in range(n)]

stack = []
answer = 0
cur = 0
for i in range(n):
    if info[i][0] == 1:
        stack.append([i, info[i][2] - 1])
    elif stack:
        stack[-1][1] -= 1

    if stack and stack[-1][1] <= 0:
        answer += info[stack[-1][0]][1]
        stack.pop()
print(answer)
