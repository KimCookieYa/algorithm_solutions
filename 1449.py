import sys

input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

b = 0
answer = n
for i in range(n):
    if a[i] <= b:
        answer -= 1
    else:
        b = a[i] + l - 1

print(answer)
