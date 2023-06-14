import sys
input = sys.stdin.readline

str1 = list(input().strip())
str2 = list(input().strip())

dp = [0] * len(str2)
for c in str1:
    cnt = 0
    for i in range(len(str2)):
        if cnt < dp[i]:
            cnt = dp[i]
        elif str2[i] == c:
            dp[i] = cnt+1
print(max(dp))