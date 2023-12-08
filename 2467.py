n = int(input())
arr = list(map(int, input().split()))

answer = [1000000001, 1000000001]
left = 0
right = n - 1
while left < right:
    temp = arr[left] + arr[right]
    if abs(sum(answer)) > abs(temp):
        answer = [arr[left], arr[right]]
    if temp > 0:
        right -= 1
    else:
        left += 1

print(*answer)
