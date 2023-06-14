from collections import deque
n = int(input())

dp = [0] * (n+1)
back_path = [i for i in range(n+1)]
queue = deque()
queue.append(n)
path = []
while queue:
    x = queue.popleft()
    distance = dp[x]
    
    if x == 1:
        print(distance)
        cur = 1
        while cur != n:
            path.append(cur)
            cur = back_path[cur]
        path.append(n)
        break
    
    if x > 0 and not dp[x-1]:
        queue.append(x-1)
        dp[x-1] = distance+1
        back_path[x-1] = x
    if x%3 == 0 and not dp[x//3]:
        queue.append(x//3)
        dp[x//3] = distance+1
        back_path[x//3] = x
    if x%2 == 0 and not dp[x//2]:
        queue.append(x//2)
        dp[x//2] = distance+1
        back_path[x//2] = x

print(*path[::-1])