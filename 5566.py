n, m = map(int, input().split())

a = [int(input()) for __ in range(n)]
b = [int(input()) for __ in range(m)]

x = 0
answer = 0
for c in b:
    x += c
    answer += 1
    if x >= n - 1:
        break
    x += a[x]
    if x >= n - 1:
        break

print(answer)
