import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

def qsort(arr):
    def qsort(arr, left, right):
        pivot = arr[(left+right)//2]
        pl = left
        pr = right
        
        while pl <= pr:
            while a[pl] < pivot: pl += 1
            while pivot < a[pr]: pr -= 1
            
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        
        if left < pr:
            qsort(arr, left, pr)
        if pl < right:
            qsort(arr, pl, right)
    
    n = len(arr)
    qsort(arr, 0, n-1)

def solution(arr, m):
    def binarySearch(arr, left, right):
        global answer
        if left == right:
            if solution(arr, m, left):
                return 1
            return 0
        elif left > right:
            return 0
        
        center = (left+right)//2
        isBig = solution(arr, m, center)
        if not isBig:
            return binarySearch(arr, left, center)
        elif isBig:
            answer = max(answer, center)
            return binarySearch(arr, center+1, right)
    
    def solution(arr, m, h):
        result = 0
        for item in arr[::-1]:
            if item > h:
                result += item-h
            if result >= m:
                return True
        
        return False
    
    n = len(arr)
    
    binarySearch(arr, 0, arr[-1])
    # answer = arr[-1]
    # for limit in range(answer, -1, -1):
    #     if solution(arr, m, limit):
    #         return limit

# qsort(a)
# answer = 0
# solution(a, m)
# print(answer)

start, end = 0, max(a)

while start <= end:
    center = (start+end)//2
    result = 0
    for item in a:
        if item >= center:
            result += item-center
    
    if result >= m:
        start = center+1
    else:
        end = center-1

print(end)