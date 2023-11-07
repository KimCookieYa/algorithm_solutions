n, b = map(int, input().split())

answer = ""
while n > 0:
    temp = n % b
    if temp >= 10:
        c = chr(temp - 10 + 65)
    else:
        c = str(temp)

    answer = c + answer
    n = n // b

print(answer)
