def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def fraction(a: list, b: list, c: list):
    child = a[0] * b[1] * c[0] + a[1] * b[0] * c[1]
    parent = a[1] * b[1] * c[0]

    temp = gcd(child, parent)
    return [child // temp, parent // temp]


n = int(input())

equation = input().split()

stack = []
for i in range(n):
    if equation[i] == "(":
        stack.append("(")
    elif equation[i] == ")":
        c = stack.pop()
        b = stack.pop()
        a = stack.pop()
        stack.pop()
        temp = fraction(a, b, c)
        stack.append(temp)
    else:
        stack.append([int(equation[i]), 1])

if len(stack) > 1:
    print(-1)
elif stack[0] == "(" or stack[0] == ")":
    print(-1)
else:
    print(*stack[0])
