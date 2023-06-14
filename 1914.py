def hanoi(x, start, rest, end):
    if x <= 1:
        print(f'{start} {end}')
        return
    
    hanoi(x-1, start, end, rest)
    print(f'{start} {end}')
    hanoi(x-1, rest, start, end)

n = int(input())
print(2**n-1)
if n < 21:
    hanoi(n, 1, 2, 3)