n = 28

answer = [i + 1 for i in range(30)]
for i in range(n):
    temp = int(input())
    answer[temp - 1] = 100
answer.sort()
print(answer[0])
print(answer[1])
