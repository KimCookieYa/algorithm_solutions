import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())

answer = []
leftheap = []
rightheap = []
for _ in range(n):
    x = int(input())
    
    if len(leftheap) == len(rightheap):
        hq.heappush(leftheap, -x)
    else:
        hq.heappush(rightheap, x)
    
    if rightheap and -leftheap[0] > rightheap[0]:
        minVal = hq.heappop(rightheap)
        maxVal = -hq.heappop(leftheap)
        hq.heappush(leftheap, -minVal)
        hq.heappush(rightheap, maxVal)
        
    answer.append(-leftheap[0])

for i in answer:
    print(i)