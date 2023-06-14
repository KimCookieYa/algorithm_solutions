import sys

input = sys.stdin.readline

n, m = map(int, input().split())
chess = [input() for __ in range(n)]


def solution(sx, sy):
    result = 0
    color = chess[sy][sx]
    for i in range(sy, sy + 8):
        for j in range(sx, sx + 8):
            if chess[i][j] != color:
                result += 1
            if color == "W":
                color = "B"
            else:
                color = "W"
        if color == "W":
            color = "B"
        else:
            color = "W"

    result = min(result, 64 - result)
    return result


answer = int(10**9)
for i in range(n - 7):
    for j in range(m - 7):
        temp = solution(j, i)
        if answer > temp:
            answer = temp

print(answer)
