import sys

input = sys.stdin.readline

n = 5
arr = []
v = 0
for i in range(n):
    arr.append(input().strip())
    if v < len(arr[i]):
        v = len(arr[i])

for i in range(v):
    for j in range(n):
        if len(arr[j]) > i:
            print(arr[j][i], end="")
