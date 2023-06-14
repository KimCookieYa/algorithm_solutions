import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushis = [int(input()) for __ in range(n)]
sushis += sushis

answer = 0
for i in range(n):
    temp = sushis[i : i + k] + [c]
    temp = list(set(temp))
    result = len(temp)
    if answer < result:
        answer = result

print(answer)
