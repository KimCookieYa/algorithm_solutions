t = int(input())
while t > 0:
    ox = input()
    score = 0
    check = 1
    for result in ox:
        if result == 'O':
            score += check
            check += 1
        else:
            check = 1
    print(score)
    t -= 1