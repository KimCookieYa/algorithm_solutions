n = input().strip()

if n[0] == "0":
    print(0)
else:
    dp = [0] * (len(n) + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(n) + 1):
        if n[i - 1] == "0" and n[i - 2] == "0":
            break
        if n[i - 2] == "1":
            if n[i - 1] == "0":
                dp[i - 1] = 0
            dp[i] = dp[i - 2]
        elif n[i - 2] == "2":
            if 0 < int(n[i - 1]) <= 6:
                dp[i] = dp[i - 2]
            elif int(n[i - 1]) == 0:
                dp[i - 1] = 0
                dp[i] = dp[i - 2]
        elif n[i - 1] == "0":
            break
        dp[i] = (dp[i] + dp[i - 1]) % 1000000

    print(dp[-1] % 1000000)
