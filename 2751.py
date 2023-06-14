import sys

input = sys.stdin.readline
n = int(input())

a = [int(input()) for _ in range(n)]

def mergesort(a):
    def mergesort(a, left, right):
        if left >= right:
            return
        
        center = (left+right)//2
        mergesort(a, left, center)
        mergesort(a, center+1, right)
        
        p = j = 0
        i = k = left
        
        while i <= center:
            buff[p] = a[i]
            p += 1
            i += 1
        
        while j < p and i <= right:
            if buff[j] < a[i]:
                a[k] = buff[j]
                j += 1
            else:
                a[k] = a[i]
                i += 1
            k += 1
        
        while j < p:
            a[k] = buff[j]
            j += 1
            k += 1

    n = len(a)
    buff = [None] * n
    mergesort(a, 0, n-1)
    del buff

def heapsort(a):
    def heapsort(a, left, right):
        parent = left
        temp = a[parent]
        
        while parent < (right+1) // 2:
            cl = parent*2 + 1
            cr = cl+1
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp
        return

    n = len(a)
    
    ## heapify
    for i in range((n-1)//2, -1, -1):
        heapsort(a, i, n-1)
    
    ## sort
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapsort(a, 0, i-1)

#mergesort(a)
heapsort(a)
for i in a:
    print(i)