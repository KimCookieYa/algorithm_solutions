n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
arr.reverse()

print(arr[k - 1])
