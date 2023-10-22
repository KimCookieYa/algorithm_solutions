n = 20

d = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

scores = [input().split() for __ in range(n)]
answer = 0
sum = 0
for score in scores:
    if score[2] == "P":
        continue
    answer += float(score[1]) * d[score[2]]
    sum += float(score[1])
answer /= sum
print(format(answer, ".6f"))
