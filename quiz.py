n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

def qsort(a):
    def qsort(a, left, right):
        pivot = a[(left+right)//2]
        pl = left
        pr = right
        
        while pl <= pr:
            while a[pl] < pivot:
                pl += 1
            while pivot < a[pr]:
                pr -= 1
            
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        
        if left < pr:
            qsort(a, left, pr)
        if pl < right:
            qsort(a, pl, right)
    
    qsort(a, 0, len(a)-1)

print('')
qsort(a)
for i in range(n):
    print(a[i])