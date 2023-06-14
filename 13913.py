from collections import deque
import sys
input = sys.stdin.readline

def print_path(x):
    arr = []
    temp = x
    for __ in range(distance[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

n, k = map(int, input().split())
distance = [0] * 100001
move = [0] * 100001

queue = deque()
queue.append(n)
while queue:
    x= queue.popleft()
    
    if x == k:
        print(distance[x])
        print_path(x)
        break
    
    for next in [x+1, x-1, x*2]:
        if 0 <= next <= 100000:
            if distance[next] == 0:
                distance[next] = distance[x] + 1
                move[next] = x
                queue.append(next)