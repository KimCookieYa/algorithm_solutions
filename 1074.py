n, r, c = map(int, input().split())
answer = 0

def z(n, sr, sc):
    global answer, r, c
    
    if sr == r and sc == c:
        return answer
    elif n == 0:
        return answer
    
    k = 2**(n-1)
    
    if r < sr+k and c < sc+k:
        return z(n-1, sr, sc)
    elif r < sr+k and c >= sc+k:
        return k*k + z(n-1, sr, sc+k)
    elif r >= sr+k and c < sc+k:
        return 2*k*k + z(n-1, sr+k, sc)
    elif r >= sr+k and c >= sc+k:
        return 3*k*k + z(n-1, sr+k, sc+k)

print(z(n, 0, 0))