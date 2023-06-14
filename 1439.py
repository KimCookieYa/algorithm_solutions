import sys
sys.setrecursionlimit(10**9)

s = input().strip()

def solution(left, right, num):
    if left >= right:
        return
    
    global answer
    
    pl, pr = left, right
    while pl < right and s[pl] == num: pl += 1
    while left < pr and s[pr] == num: pr -= 1
    
    if num == '0':
        num = '1'
    else:
        num = '0'
    
    if pl <= pr:
        answer += 1
        solution(pl, pr, num)

answer = 0
solution(0, len(s)-1, s[0])
print(answer)