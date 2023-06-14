import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
sade = list(map(int, input().split()))
sade.sort()

def bsearch(left, right, target):
    while left <= right:
        mid = (left+right)//2
        if sade[mid] < target:
            left = mid+1
        elif sade[mid] > target:
            right = mid-1
        else:
            return mid
    return right

answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y > l:
        continue
    
    idx = bsearch(0, m-1, x)
    for k in [idx-1, idx, idx+1]:
        if 0 <= k and k < m:
            if y + abs(sade[k]-x) <= l:
                answer += 1
                break
    
print(answer)