a, b = map(int, input().split())

answer = 0
while b != a and b > 0:
    if b%10 == 1:
        b = b//10
    elif b%2 == 0:
        b = b//2
    else:
        break
    answer += 1

if b == a:
    print(answer+1)
else:
    print(-1)