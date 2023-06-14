import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

answer = 0
height = 0
for item in a[::-1]:
    if height < item:
        height = item
        answer += 1

print(answer)