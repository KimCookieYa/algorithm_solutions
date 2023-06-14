a = [0] * 9
for i in range(9):
    a[i] = int(input())

check = 0
sum_val = sum(a)
for i in range(9):
    for j in range(i+1, 9):
        if i != j and sum_val-a[i]-a[j] == 100:
            a = a[:i] + a[i+1:j] + a[j+1:]
            check = 1
            break
    if check == 1:
        break

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

qsort(a)
for i in range(7):
    print(a[i])