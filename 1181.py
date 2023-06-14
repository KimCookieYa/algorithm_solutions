n = int(input())

a = {}
for i in range(n):
    a[input()] = 1
a = list(a.keys())

def isBig(sa, sb):
    if len(sa) < len(sb):
        return True
    elif len(sa) > len(sb):
        return False
    
    for a, b in zip(sa, sb):
        if a < b:
            return True
        elif a > b:
            return False
    
    return False

def quicksort(a):
    def quicksort(a, left, right):
        pivot = a[(left+right)//2]
        pl = left
        pr = right
        
        while pl <= pr:
            while isBig(a[pl], pivot):
                pl += 1
            while isBig(pivot, a[pr]):
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

quicksort(a)
for i in a:
    print(i)