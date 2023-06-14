n = int(input())

answer = 0
cur = n
while True:
    cur = 10*(cur%10) + ((cur//10)+(cur%10))%10
    
    answer += 1
    if cur == n:
        break

print(answer)