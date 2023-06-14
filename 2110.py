import sys
input = sys.stdin.readline

n, c = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = int(input())

a.sort()

def bsearch(arr, start, end):
    answer = 0
    while start <= end:
        mid = (start+end)//2
        cur = arr[0]
        count = 1
        
        for i in range(1, len(arr)):
            if arr[i] >= cur + mid:
                count += 1
                cur = arr[i]
        
        if count >= c:
            start = mid+1
            answer = mid
        else:
            end = mid-1
    
    return answer

print(bsearch(a, 0, a[-1]-a[0]))