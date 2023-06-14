n = input()
n = n.replace("9", "6")

answer = 0
for i in range(9):
    if i != 6:
        answer = max(answer, n.count(str(i)))
    else:
        answer = max(answer, (n.count(str(i)) + 1) // 2)

print(answer)
