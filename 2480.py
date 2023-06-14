dice = list(map(int, input().split()))
set_dice = list(set(dice))

if len(set_dice) == 1:
    print(10000 + set_dice[0]*1000)
elif len(set_dice) == 2:
    for i in range(3):
        if dice.count(dice[i]) == 2:
            break
    print(1000 + dice[i]*100)
else:
    print(max(dice) * 100)