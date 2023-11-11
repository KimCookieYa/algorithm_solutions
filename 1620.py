import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = dict()
for i in range(n):
    a = input().strip()
    arr[i + 1] = a
    arr[a] = i + 1

for i in range(m):
    a = input().strip()
    if a.isdigit():
        a = int(a)
        print(arr[a])
    else:
        print(arr[a])
