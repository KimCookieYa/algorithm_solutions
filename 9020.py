t = int(input())

def isPrime(x):
    if x == 1:
        return False
    
    for i in range(2, int(x**0.5)+1):
        if x // i > 1 and x % i == 0:
            return False
    return True

while t > 0:
    n = int(input())
    for i in range(n//2, 1, -1):
        if isPrime(i) and isPrime(n-i):
            print(f'{i} {n-i}')
            break
    
    t -= 1