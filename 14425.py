import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_arr = [input().strip() for __ in range(n)]

answer = 0
for __ in range(m):
    a = input().strip()
    if a in n_arr:
        answer += 1

print(answer)
