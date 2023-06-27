n, m = map(int, input().split())
buckets = [0] * n
for __ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j + 1):
        buckets[idx - 1] = k
print(*buckets)
