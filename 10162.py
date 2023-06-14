t = int(input())

answer = []
minutes = [300, 60, 10]
for minute in minutes:
    answer.append(t // minute)
    t = t % minute
if t == 0:
    print(*answer)
else:
    print(-1)