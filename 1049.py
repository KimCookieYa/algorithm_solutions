n, m = map(int, input().split())
costs = [list(map(int, input().split())) for __ in range(m)]

min_package = min([cost[0] for cost in costs])
min_piece = min([cost[1] for cost in costs])

answer = 0
if min_package <= min_piece * 6:
    answer = min_package * (n//6) + min_piece * (n%6)
    if min_package < min_piece * (n%6):
        answer = min_package * (n//6 + 1)
else:
    answer = min_piece * n

print(answer)