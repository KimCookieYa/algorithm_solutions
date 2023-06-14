import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
train = [[0, 0] for _ in range(n)]
for i in range(n):
    l, r = map(int, input().split())
    if l > r:
        train[i] = [r, l]
    else:
        train[i] = [l, r]
d = int(input())

train.sort(key=lambda x: x[1])

answer = 0
heap = []
for s, e in train:
    lim = e - d
    if s >= lim:
        heappush(heap, s)
    while heap and heap[0] < lim:
        heappop(heap)
    answer = max(answer, len(heap))
print(answer)