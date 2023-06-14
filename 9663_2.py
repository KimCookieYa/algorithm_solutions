import sys
n = int(sys.stdin.readline())

def n_queen(n):
    def n_queen(n, row, r):
        global answer
        
        if r == n:
            answer += 1
            return
        
        for i in range(n):
            for j in range(r):
                if row[j] == i or r-j == abs(row[j]-i):
                    break
            else:
                row[r] = i
                n_queen(n, row, r+1)
    
    row = [None] * (n+1)
    n_queen(n, row, 0)
    
answer = 0
n_queen(n)
print(answer)