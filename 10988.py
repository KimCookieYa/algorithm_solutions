s = input().strip()
n = len(s)
answer = 0
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        break
else:
    answer = 1

print(answer)
