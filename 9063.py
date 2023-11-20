import sys

input = sys.stdin.readline

n = int(input())
start = [10000, 10000]
end = [-10000, -10000]

for __ in range(n):
    point = list(map(int, input().split()))
    if start[0] > point[0]:
        start[0] = point[0]
    if start[1] > point[1]:
        start[1] = point[1]
    if end[0] < point[0]:
        end[0] = point[0]
    if end[1] < point[1]:
        end[1] = point[1]

print((end[0] - start[0]) * (end[1] - start[1]))
