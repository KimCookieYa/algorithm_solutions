a, b, c = map(int, input().split())

d = max(a, b, c)
v = a + b + c - d
for e in range(d, 0, -1):
    if e < v:
        v += e
        break
print(v)
