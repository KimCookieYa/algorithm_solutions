n = int(input())

def solution(n):
    if n == 1:
        return dp[0]

    m = n//3
    result = []
    prev = solution(m)
    for p in prev:
        result.append(p*3)
    for p in prev:
        result.append(p+' '*(n//3)+p)
    for p in prev:
        result.append(p*3)
    return result

dp = [['*'] for __ in range(8)]
temp = n
print('\n'.join(solution(n)))