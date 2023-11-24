n = int(input())
k = int(input())
points = list(map(int, input().split()))
points.sort()

arr = [points[i + 1] - points[i] for i in range(n - 1)]
arr.sort(reverse=True)

for __ in range(k - 1):
    if len(arr) > 0:
        arr.pop(0)

print(sum(arr))
