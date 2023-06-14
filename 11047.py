import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for __ in range(n)]

left = 0
right = n-1
while left <= right:
    mid = (left+right)//2
    if a[mid] < k:
        left = mid+1
    elif a[mid] > k:
        right = mid-1
    else:
        break

answer = 0
for i in range(mid, -1, -1):
    if k >= a[i]:
        answer += k // a[i]
        k = k % a[i]

print(answer)