n, m = map(int, input().split())

arr = [list(map(int, input().split())) for __ in range(m)]
answer = [i + 1 for i in range(n)]
for a in arr:
    temp = answer[a[0] - 1]
    answer[a[0] - 1] = answer[a[1] - 1]
    answer[a[1] - 1] = temp

print(*answer)
