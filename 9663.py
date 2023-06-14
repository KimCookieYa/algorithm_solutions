n = int(input())

def n_queen(n):
    def print_chess_map(n):
        for i in range(n):
            print(chess_map[i])
        print('')
    
    def check_visited(visited, x, y):
        for i in range(x+1, n):
            for j in range(3):
                nx = x + (i-x) * dir[j][0]
                ny = y + (i-x) * dir[j][1]
                if ny < 0 or ny >= n:
                    continue
                chess_map[ny][nx] += visited

    def n_queen(n, x, y):
        if x == n-1:
            return 1
        
        val = 0
        check_visited(1, x, y)
        for i in range(n):
            if chess_map[i][x+1] == 0:
                val += n_queen(n, x+1, i)
        check_visited(-1, x, y)
        
        return val
    
    dir = [[1, -1], [1, 0], [1, 1]]
    answer = 0
    chess_map = [[0 for _ in range(n)] for _ in range(n)]
    for k in range(n):
        answer += n_queen(n, 0, k)
    return answer

answer = n_queen(n)
print(answer)