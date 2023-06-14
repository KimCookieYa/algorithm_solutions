import sys

input = sys.stdin.readline

n = int(input())
grades = [int(input()) for __ in range(n)]
grades.sort()

answer = 0
for i, item in enumerate(grades):
    answer += abs(item - i - 1)
print(answer)
