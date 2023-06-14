import sys

input = sys.stdin.readline

locks = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, -1, -1]]

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def solution(n, x, y):
    if n == 1:
        return 1

    result = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 3 and 0 <= ny < 4:
            if locks[ny][nx] != -1:
                result += solution(n - 1, nx, ny)
    return result


def solution2(m):
    for i in range(1, m + 1):
        for j in range(10):
            x = j % 3
            y = j // 3
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < 3 and 0 <= ny < 4:
                    if locks[ny][nx] != -1:
                        a = locks[ny][nx] - 1
                        if a < 0:
                            a = 9
                        passwords[i][j] += passwords[i - 1][a] % 1234567


t = int(input())
passwords = [[0 for i in range(10)] for __ in range(1001)]
passwords[0] = [1 for i in range(10)]

n = [int(input()) for __ in range(t)]
solution2(max(n))

for i in range(t):
    print(sum(passwords[n[i] - 1]) % 1234567)

# for __ in range(t):
#     n = int(input())

#     answer = 0
#     for i in range(10):
#         answer += solution(n, i % 3, i // 3)
#     print(answer)
