def solution(n):
    if n == 0:
        return dp[n]
    
    prev = solution(n-1)
    m = 3**(n-1)
    dp[n] = prev + ' ' * m + prev
    return dp[n]
    

nn = []
while True:
    try:
        n = input()
        if n == "":
            break
        nn.append(int(n))
    except:
        break

dp = [[] for __ in range(13)]
dp[0] = '-'
for n in nn:
    print(''.join(solution(n)))