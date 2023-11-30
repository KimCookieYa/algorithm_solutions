from collections import deque

n, k = map(int, input().split())

dp = [100000] * 100001
dp[n] = 0

q = deque()
q.append(n)
while q:
    cur = q.popleft()

    if cur == k:
        break

    if cur - 1 >= 0:
        if dp[cur - 1] > dp[cur] + 1:
            dp[cur - 1] = dp[cur] + 1
            q.append(cur - 1)
    if cur + 1 <= 100000:
        if dp[cur + 1] > dp[cur] + 1:
            dp[cur + 1] = dp[cur] + 1
            q.append(cur + 1)
    if 0 <= 2 * cur <= 100000:
        if dp[2 * cur] > dp[cur]:
            dp[2 * cur] = dp[cur]
            q.append(2 * cur)

print(dp[k])
