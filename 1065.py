n = int(input())

if n < 100:
    print(n)
else:
    answer = 99
    for i in range(100, n+1):
        first = i % 10
        second = (i//10) % 10
        third = i//100
        
        if (third - second) == (second - first):
            answer += 1

    print(answer)