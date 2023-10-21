n = input()
m = len(n)
n = int(n)

answer = (n - pow(10, m - 1) + 1) * m
while m > 1:
    answer += (pow(10, m - 2) * 9) * (m - 1)
    m -= 1
print(answer)
