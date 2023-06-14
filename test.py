def check_visited(visited, x, y):
    n = 5
    chess_map = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == y or j == x or abs(x-j) == abs(y-i):
                chess_map[i][j] += visited
    
    for _ in range(n):
        print(chess_map[_])

check_visited(-1, 3, 1)