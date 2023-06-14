a, b, c = map(int, input().split())

def solution(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    
    return ((solution(a, b//2, c) ** 2 % c) * solution(a, b%2, c)) % c

print(solution(a, b, c))