import sys
input = sys.stdin.readline

n, m = map(int, input().split())
smalls = [int(input())-1 for __ in range(m)]

dp = [[] for __ in range(n)]
dp[0] = [0]
dp_step = [[] for __ in range(n)]
dp_step[0] = [0]

for step in range(n):
    if step in smalls:
        continue
    
    idx = 0
    for cur_step in dp_step[step]:
        for next_step in [cur_step-1, cur_step, cur_step+1]:
            next = step+next_step
            if step < next < n:
                if next not in smalls:
                    if dp[step][idx]+1 not in dp[next] and next_step not in dp_step[next]:
                        dp[next].append(dp[step][idx]+1)
                        dp_step[next].append(next_step)
        idx += 1

if dp[n-1] == []:
    print(-1)
else:
    print(min(dp[n-1]))