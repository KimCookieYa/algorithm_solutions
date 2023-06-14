n = int(input())

money = 1000-n
answer = 0
coins = [500, 100, 50, 10, 5, 1]
for coin in coins:
    answer += money // coin
    money = money % coin
    if money == 0:
        break

print(answer)