import sys
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    n = int(input())
    scores = [list(map(int, input().split())) for __ in range(n)]
    scores.sort()
    
    answer = 1
    winner = scores[0][1]
    for i in range(1, n):
        print('scores', scores[i])
        if winner > scores[i][1]:
            winner = scores[i][1]
            answer += 1
    print(answer)