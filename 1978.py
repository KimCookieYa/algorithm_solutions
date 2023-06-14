n = int(input())
a = map(int, input().split())


def isPrime(x):
    if x == 1:
        return False
    
    for i in range(2, (int(x**0.5)+1)):
        if x // i > 1 and x % i == 0:
            return False
    return True

print(len(list(filter(lambda x: isPrime(x), a))))

# print(sum(1 < i * all(i%j for j in range(2, i)) for i in a))

# for i in a:
#     print(1 < i * all(i%j for j in range(2, i)))