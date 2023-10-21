a = input()
b = input()

i = 0
answer = 0
c = len(b)
while i < len(a):
    if b == a[i : i + c]:
        answer += 1
        i += c
    else:
        i += 1

print(answer)
