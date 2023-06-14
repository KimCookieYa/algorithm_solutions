s = int(input())

answer = 1
while True:
    if answer * (answer+1) // 2 > s:
        answer -= 1
        break
    answer += 1

print(answer)