from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
buildings = [list(map(int, input().split())) for _ in range(n)]
buildings.sort(key=lambda x: (x[0], -x[1]))

answer_heap = []

heap = []
for building in buildings:
    while heap and heap[0][1] < building[0]:
        heappop(heap)
    
    if heap:
        if answer_heap[-1][0] == building[0]:
            continue
        if -heap[0][0] < building[1]:
            heappush(answer_heap, (building[0], building[1]))
    else:
        heappush(answer_heap, (building[0], building[1]))

    heappush(heap, (-building[1], building[2]))


buildings.sort(key=lambda x: (x[2], -x[1]))
heap = []
for building in buildings[::-1]:
    while heap and heap[0][1] > building[2]:
        heappop(heap)
    
    if heap:
        if answer_heap[-1][0] == building[2]:
            continue
        if -heap[0][0] < building[1]:
            heappush(answer_heap, (building[2], -heap[0][0]))
    else:
        heappush(answer_heap, (building[2], 0))
    
    heappush(heap, (-building[1], building[0]))

while answer_heap:
    print(*heappop(answer_heap), end=' ')