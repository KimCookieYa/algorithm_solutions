from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    heappush(a, int(input()))

answer = 0

if n == 1:
    answer = 0
else:
    while len(a) > 1:
        sumVal = heappop(a) + heappop(a)
        answer += sumVal
        heappush(a, sumVal)

print(answer)