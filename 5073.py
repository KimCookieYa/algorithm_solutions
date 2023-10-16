import sys

input = sys.stdin.readline


def isTriangle(a, b, c):
    if max(a, b, c) >= a + b + c - max(a, b, c):
        return False
    return True


while True:
    [a, b, c] = list(map(int, input().split()))
    if a == b == c == 0:
        break
    if not isTriangle(a, b, c):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b != c or a == c != b or b == c != a:
        print("Isosceles")
    elif a != b != c:
        print("Scalene")
