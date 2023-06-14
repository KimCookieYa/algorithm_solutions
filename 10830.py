n, b = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


def production(A, B):
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j] % 1000
                C[i][j] = C[i][j] % 1000
    return C

def power(A):
    return production(A, A)

def solution(A, b):
    if b == 0:
        C = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            C[i][i] = 1
        return C
    elif b == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] %= 1000
        return A
    return production(solution(A, b%2), power(solution(A, b//2)))

answer = solution(mat, b)
for i in range(n):
    print(*answer[i])