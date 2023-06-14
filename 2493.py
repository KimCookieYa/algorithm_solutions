import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

stack = [n-1]
for i in range(n-2, -1, -1):
    if a[stack[-1]] > a[i]:
        stack.append(i)
    else:
        while stack and a[stack[-1]] < a[i]:
            cur = stack.pop()
            a[cur] = i+1
        stack.append(i)

while stack:
    cur = stack.pop()
    a[cur] = 0

print(*a)