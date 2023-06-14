n = int(input())

a = []
while n > 0:
    a.append(int(input()))
    n -= 1

def quicksort(a, left, right):
    pivot = a[(left+right)//2]
    pl = left
    pr = right
    while pl <= pr:
        while pivot > a[pl]:
            pl += 1
        while pivot < a[pr]:
            pr -= 1
            
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    if left < pr:
        quicksort(a, left, pr)
    if pl < right:
        quicksort(a, pl, right)

quicksort(a, 0, len(a)-1)
    
for i in a:
    print(i)