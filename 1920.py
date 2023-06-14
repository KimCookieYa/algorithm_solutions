import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

def qsort(arr):
    def qsort(arr, left, right):
        pivot = arr[(left+right)//2]
        pl = left
        pr = right
        
        while pl <= pr:
            while arr[pl] < pivot: pl += 1
            while pivot < arr[pr]: pr -= 1
            
            if pl <= pr:
                arr[pl], arr[pr] = arr[pr], arr[pl]
                pl += 1
                pr -=1
        
        if left < pr:
            qsort(arr, left, pr)
        if pl < right:
            qsort(arr, pl, right)

    n = len(arr)
    qsort(arr, 0, n-1)

def binarySearch(arr, target):
    def binarySearch(arr, target, left, right):
        if left == right:
            if arr[left] == target:
                return 1
            return 0
        
        center = (left+right)//2
        if target <= arr[center]:
            return binarySearch(arr, target, left, center)
        elif target > arr[center]:
            return binarySearch(arr, target, center+1, right)
        elif target == arr[center]:
            return 1
    
    n = len(arr)
    return binarySearch(arr, target, 0, n-1)


qsort(a)
for i in range(len(b)):
    print(binarySearch(a, b[i]))