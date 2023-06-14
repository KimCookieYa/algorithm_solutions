n = int(input())
a = list(map(int, input().split()))


def bsearch(left, right, target):
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right


arr = [a[0]] + [0] * 1000
idx = 0
for i in range(1, n):
    if arr[idx] < a[i]:
        idx += 1
        arr[idx] = a[i]
    else:
        temp = bsearch(0, idx, a[i])
        arr[temp] = a[i]

print(idx + 1)
