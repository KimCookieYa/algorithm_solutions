n, b = input().split()

b = int(b)
A = ord("A")
answer = 0
for c in n:
    if c.isdigit():
        answer = answer * b + int(c)
    else:
        answer = answer * b + ord(c) - A + 10

print(answer)
