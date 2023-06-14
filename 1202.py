from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
diamonds = []
for __ in range(n):
    heappush(diamonds, list(map(int, input().split())))
bags = [int(input()) for __ in range(k)]
bags.sort()

temp = []
answer = 0
for i in range(k): 
    while diamonds and bags[i] >= diamonds[0][0]:
        heappush(temp, -heappop(diamonds)[1])
    
    if temp:
        answer -= heappop(temp)
    elif not diamonds:
        break

print(answer)