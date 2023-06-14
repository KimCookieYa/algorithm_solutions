import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visited = list(map(int, input().split()))

answer = sum(visited[:x])
lst = [sum(visited[:x])]
for i in range(1, n - x + 1):
    a = lst[i - 1] - visited[i - 1] + visited[i + x - 1]
    if answer < a:
        answer = a
    lst.append(a)

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(lst.count(answer))
