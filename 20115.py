import heapq
import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))
heap = []
for i in range(n):
    heapq.heappush(heap, -drinks[i])

answer = -heapq.heappop(heap)
for i in range(1, n):
    answer += -heapq.heappop(heap)/2

if int(answer) == answer:
    print(int(answer))
else:
    print(round(answer, 6))