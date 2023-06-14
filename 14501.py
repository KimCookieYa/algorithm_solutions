n = int(input())
tp = []
for _ in range(n):
    temp = input().split()
    tp.append([int(temp[0]), int(temp[1])])
tp.append([0, 0])

dp = [0] * (n+1)
for i in range(n+1):
    nxt = tp[i][0]+i
    if nxt < n+1:
        for j in range(nxt, n+1):
            dp[j] = max(dp[j], dp[i] + tp[i][1])
        
#print(dp)
print(max(dp))