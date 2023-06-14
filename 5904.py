n = int(input())

s = "moo"
length = 3
idx = 0
dp = [3]
while True:
    length = 2*length + idx + 4
    dp.append(length)
    idx += 1
    if length > n:
        break

def solution(left, idx, n):
    if idx < -1:
        return s[n]
    
    if n < dp[idx]:
        return solution(left, idx-1, n)
    elif n >= idx+4 + dp[idx]:
        return solution(left, idx-1, n-(idx+4+dp[idx]))
    else:
        if n - dp[idx] == 0:
            return 'm'
        else:
            return 'o'

print(solution(0, idx-1, n-1))